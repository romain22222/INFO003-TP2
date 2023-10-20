# INFO003 - TP2

## Partie 1
### Lancement

`python3 .\allCall.py <Path vers le json de test>`

Vous trouverez un exemple de json de test dans le dossier `jsons`

Si vous voulez tester un algorithme sur une instance en particulier, vous pouvez entrer la commande

`python3 .\main.py <backtracking/random/lawler> <Path vers l'instance à tester>`

Pour tester une solution, vous pouvez entrer la commande

`python3 .\main.py verif <Path vers l'instance à tester> "Solution à tester"`

Les deux premières commandes afficheront le résultat de l'algorithme sous la forme :
`[<Est-ce qu'une solution a été trouvée>, <Tableau des couleurs trouvées résolvant 3-couleur>]`

La dernière affichera :

`[<Est-ce que la solution est valide>, <Si la solution n'est pas valide, renvoie la première arête qui pose problème>]`

### Complexités

Pour le backtracking et lawler, les complexités sont exponentielles. Pour le random, la complexité est quadratique.

Pour random, on trouve la solution en moyenne une fois sur 2, mais il semble que cela dépend du nombre de sommets et d'arêtes.

## Partie 2

### Lancement
