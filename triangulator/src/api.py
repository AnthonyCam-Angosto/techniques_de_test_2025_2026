"""Ce module s'occupe de gére l'api."""
import uuid

from flask import Flask

from src import conversion, pointSetManager, triangulation

app=Flask(__name__)


@app.route("/triangulation/<pointsetid>", methods=['GET'])
def get_triangulation(pointsetid):
    """Requete principal de l'api.
    
    Params:
        pointSetId(str):identifiant du pointSet en uuid
    
    Returns:
        reponse(str)
        code(int)

    """
    try:
        uuid.UUID(pointsetid)
    except ValueError:
        return "Bad request, e.g., invalid PointSetID format.",400
    
    pointset_bin=pointSetManager.appel(pointsetid)

    if(isinstance(pointset_bin,int)):
        if(pointset_bin==2):
            return "A PointSet with the specified ID was not found.",404
        else:
            message="Service unavailable: communication with PointSetManager failed."
            return message,503

    try:
        pointset=conversion.conversion_point(pointset_bin)
        triangles=triangulation.start(pointset)
        result=conversion.conversion_triangle(triangles)
        return result,200
    
    except Exception:
        return "Internal server error, e.g., triangulation algorithm failed.",500
