from flask import Flask

app=Flask(__name__)

@app.route("/triangulation/str:<pointSetId>", methods=['GET'])
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