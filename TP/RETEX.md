# RETEX – Retour d'expérience sur le projet

Ce projet m'a permis d'appliquer la méthode **"test first"**, que j'avais déjà étudiée mais jamais mise en pratique.


## Points positifs 
- les test pour l'API et la conversion était bon
- les différent cas de test surtout les test d'integraction qui m'a permit de corrige un bug

## Points négatifs
- Changement de la fonction pour l'appel vers une autre API, ce qui a modifié le mock  
- Ajout d'un test en doublon dans la conversion triangulaire 
- Modification de certains tests pour remplacer le retour par une erreur plutôt qu'une valeur vide  
- La conversion et la triangulation ne produisaient pas les données dans le même ordre que celles des tests, ce qui entraînait des échecs

## Analyse rétrospective du plan initial

J'aurais dû mieux gérer les données de test et intégrer la gestion des erreurs dès le début plutot que faire avec des retour de valeur null

le principal défaut du plan résidait dans la taille des données utilisées pour les tests de performance, ainsi que dans l'ajout tardif d'un test supplémentaire. À part cela, le plan était globalement solide.
