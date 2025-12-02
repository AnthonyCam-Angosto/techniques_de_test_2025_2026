from flask import Flask

app=Flask(__name__)


#/str:<pointSetId>"
@app.route("/triangulation", methods=['GET'])
def triangulation(pointsetid:str):
    """
    requete principal de l'api
    Params:
        pointSetId(str):identifiant du pointSet en uuid
    
    Returns:
        reponse(str)
        code(int)
    """
    return "not implemented",201
