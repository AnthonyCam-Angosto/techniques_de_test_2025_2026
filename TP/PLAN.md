## test performance
1. temps de traitement de la triangulation :
    - test avec un triangle pour avoir le temps le plus court
    - test avec une 10 ou 15 de point pour avoir un temps moyen
    - test avec une 20 ou 30 pour avoir le cas d'une situation complexe

2. temps de traitement de la conversion des triangles vers le binaire :
    - test avec 1 triangles pour avoir le temps le plus court
    - test avec une 10 triangles pour avoir un temps moyen
    - test avec une 20 triangles pour avoir le cas d'une situation complexe

3. temps de traitement de la conversion d'un PointSet depuis le binaire :
    - test avec 3 point pour avoir le temps le plus court
    - test avec une 20 de point pour avoir un temps moyen
    - test avec une 40 pour avoir le cas d'une situation complexe



## test Triangulator

1. test api : tests permetant de test les requetes de cette api et de l'autre api dans une situation normal et avec erreur **(l'autre api est mocker durant ces test)**
    - cas normal appel d'une autre api : requete pour recupere PointSet
    - cas normal reception : appel de cette api
    - PointSetManager n'a pas pue se connecter avec l'API et retourne l'erreur 503
    - PointSETID n'existe pas : identifiant invalide et retourne l'erreur 404
    - PointSetID erreur format : indentifinat dans le mauvais format et retourne l'erreur 400

2. test conversion depuis le binaire : tests de la conversion du binaire en objet point n'a pas de problème 
    - cas normal : verifier qu'il retourne les bon point
    - binaire ne suit pas la structure : la suite a un bit en plus
    - donnée pas en binaire : donnée dans un autre format par exemple en int ou float
    - erreur dans le binaire sur le nombre de point : erreur sur les 4 premier bytes qui donne pas le bon nombre de point
    - donnée d'entrée NULL : donnée d'entrée n'existe pas
    - binaire vide : binaire ne contenant aucune valeur par exemple = ""

3. test conversion vers le binaire : tests de la conversion de liste de triangle vers un binaire
    - cas normal : verfier qu'il retourne le bon binaire
    - donnée d'entrée NULL : donnée d'entrée n'existe pas
    - erreur sur un triangle : triangle contient qu'un ou deux point ou erreur sur position d'un point
    - liste de triange vide : liste de triangle vide retourne un binaire contenant que les 4 premier bytes

4. test triangulation:
    - cas normal : verifier qu'il retourne bien les bon triangles (environ 10)
    - nombre de point inferieur à 3 : qu'il s'arrete sans erreur avec un résultat vide
    - donnée d'entrée NULL : qu'il retourne l'erreur 500
    - liste des points vide : qu'il retourne l'erreur 500
    - erreur sur un point(manque le x ou le y) : qu'il retourne l'erreur 500
    - point colinéaire : point sur la même ligne, cas complexe. vefier avec que des point colinéaire et un autre cas avec pas que des point colinéaire

5. creation d'un triangle :
    - cas normal : creation de l'objet triangle 
    - nombre de point inferieur ou superieur à 3 : retourne une erreur 500
    - erreur sur un point : position manquant ou vide

6. test d'integration: 
    - cas normal entre la conversion depuis le binaire vers le triangulation
    - cas normal entre le triangulation vers la conversion vers le binaire

### Comment

1. cas normal

plusieur verification sur different groupe de valeur valide pour vérifier qu'il retourne la bonne valeur

2. les autres (test d'erreur)

un seul ou deux vérification sur le cas d'erreur à verifier
