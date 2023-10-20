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

`python3 .\solve<Nom du probleme à check>.py <Path vers l'instance à tester>` <Cas du solveClique : taille de la clique recherchée>

### 1.1

Voir `solveClique.py`

### 1.2

Voir `solve3Coloration.py`

### 2.1

#### 1.

Voir `solve3CliquesCoverage.py`

#### 2. 

Sens normal : 

On peut voir que la transformation pour passer du problème de 3-coloration au problème de 3-cliques coverage est symétrique.
Donc si on a un algorithme qui résout le problème de 3-cliques coverage, on peut résoudre le problème de 3-coloration en utilisant cet algorithme sur le graphe complémentaire.
Vu que l'on a donc une réduction polynomiale du problème de 3-coloration au problème de 3-cliques coverage, alors si le problème de 3-coloration est NP-complet, alors le problème de 3-cliques coverage l'est aussi.
Sens inverse :

Vu que l'on a une réduction polynomiale du problème de 3-cliques coverage au problème de 3-coloration, si le problème de 3-cliques coverage est NP-complet, alors le problème de 3-coloration l'est aussi.

### 2.2

#### 1.

Voir `solve3SAT.py`
