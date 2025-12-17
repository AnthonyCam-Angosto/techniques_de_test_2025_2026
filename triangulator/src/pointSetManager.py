"""Ce module gere les requetes vers l'autre api."""
from urllib import request
from urllib.error import HTTPError


def appel(id:str)->str|int:
    """Fonction d'appel vers l'autre api pour recuper un pointSet.
    
    Params:
        id(str): identifiant d'un PointSet

    Returns:
        code_erreur/pointSet(int/String): de base retourne un string mais sinon retourne
        un chiffre correspondant au type d'erreur.
        1= BD indisponible, 2= id non trouver, 0= pour tout autre erreur.

    """
    try:
        request_url = request.urlopen(F'http://f"PointSetManager/pointset/{id}"')
        result=request_url.read().decode(request_url.headers.get_content_charset())
        return result
    except HTTPError as error:
        if(error.code==404):
            return 2
        elif(error.code==503):
            return 1  
    return 0