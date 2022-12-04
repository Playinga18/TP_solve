# TP_SOLVE

## 1. Prise en main de lp solve

Dans tout le TP, nous allons utiliser le programme lp solve, qui est un solveur de programmation linéaire. La documentation se trouve « ICI »
Voil`a un exemple de programme linéaire sous le format de lp solve :
```
max: 2 x1 + x2;
x1 + 2 x2 <= 20;
3.2 x1 + x2 <= 15;
```
Pour faire tourner le solveur, il suffit de taper la commande
```
$ lp_solve fichier.lp
```
Où le fichier fichier.lp contient l’exemple ci-dessus. Le r´esultat est affiché comme ceci :
```
Value of objective function: 12.77777778
Actual values of the variables:
x1      1.85185
x2      9.07407
```
Pour restreindre les solutions `a des nombres entiers, on peut ajouter la ligne suivante :
```
int x1, x2;
```


-----------------------------------------------------------

### Exercice 1:
Vérifiez que tout fonctionne correctement dans l’exemple ci-dessus. Quelles
sont les valeurs optimales de x1 et x2 si on se restreint `a des nombres entiers ?

* Voici ce que renvoie le commande `$ lp_solve` sur le fichier.lp :
```
Value of objective function: 12.00000000

Actual values of the variables:
x1                              2
x2                              8
```
* On voit donc que les valeurs optimales sont: 
x1 = 2, x2 = 8

-----------------------------------------------------------

### Exercice 2:
lp solve impose automatiquement des contraintes de non-négativité pour
toutes les variables. Essayez de changer l’objectif de l’exemple à max: -2x1+x2; et notez
que x1 ne descend pas au-dessous de 0. Vous pouvez enlever les contraintes de non-négativité
en ajoutant la ligne free x1, x2;. Essayez avec l’objectif modifié

* Lorsqu'on test le commande `$ lp_solve` avec des arguments négatifs:
```
Value of objective function: 10.00000000

Actual values of the variables:
x1                              0
x2                             10
```

* Et lorsqu'on essaye d'obtenir un chiffre negatif sur les variables, en enlevant les contraintes de
non négativité: `This problem is unbounded`

-----------------------------------------------------------

### Exercice 3:
Vérifiez que vous trouvez bien les mˆemes solutions `a l’exercice 1 de la
feuille de TD 1 avec le solveur que celles que l’on a d´etermin´ees graphiquement

* En effet les valeurs calculées graphiquement de l'exercice 1 de la feuille de td1 et les
  solutions trouvé par le solveur sont les mêmes.
-----------------------------------------------------------

## 2. Un problème générique

On considèere un problèeme plus g´en´eral o`u l’on dispose de m types de ressources R1, . . . , Rm
pour fabriquer n types de produits P1, . . . , Pn. Chaque produit j rapporte un b´en´efice de cj
pour chaque unit´e vendue.
Les diff´erentes statistiques associ´ees aux produits sont donn´ees dans un fichier texte format´e
de la fa¸con suivante :

```
3 2
250 400 490
P1 10 20 10 150
P2 10 10 25 100
```

* La premi`ere ligne indique le nombre de ressources m et de produits n.
* La deuxi`eme ligne indique les limites sur les m ressources (ex: au plus 250 unit´es de la
première ressource).
* Les n lignes qui suivent d´ecrivent les produits. La première colonne est le nom du
produit (ex: P2). Ensuite, suivent m colonnes avec les besoins en ressources (ex: 10 10
25). La dernière colonne est le b´en´efice r´ealis´e par unit´e de ce produit qui est vendue
(ex: 100).

On peut fabriquer des fractions d’unit´e de produits, et on consid`ere que tout sera vendu.
D´ezipper le fichier data.zip que vous trouvez sur elearning. Vous y trouvez quelques exemples.

-----------------------------------------------------------

### Exercice 4:
Ecrivez un programme generic.py qui prend en entrée un tel fichier et
écrit sur un autre fichier de sortie le programme linéaire associ´e. Les deux noms de fichier
seront fournis sur la ligne de commande

```
$ python3 generic.py exemple1.txt output.lp
```

Avec l’exemple ci-dessus (le fichier exemple1.txt), le contenu du fichier output.lp devrait
ressembler au suivant :

```
max: 150P1+100P2;
10P1+10P2 <= 250;
20P1+10P2 <= 400;
10P1+25P2 <= 490;
```

Ajoutez à votre programme la possibilité de donner l’argument -int sur la ligne de commande
pour rajouter des contraintes d’intégralité sur toutes les variables.

* Ci-joint le fichier generic.py ainsi que son manuel d'utilisation.

-----------------------------------------------------------

### Exercice 5:
Modifiez le programme generic.py pour qu’il lance également le solveur
lp solve avec le programme linéaire comme entrée, réecupère la solution et affiche l’optimum
ainsi que les variables non-null et leur valeurs.

Exemple avec le fichier exemple1.txt :
```
$ python3 generic.py exemple1.txt output.lp
opt = 3250
P1 = 15
P2 = 10
```

* Il suffit d'ajouter la ligne `os.system('lp_solve output.lp')` dans le main de notre programme, ainsi le programme nous permettra d'afficher les solutions et affiche l’optimum ainsi que les variables non-null et leur valeurs. 

-----------------------------------------------------------

### Exercice 6:
Essayez votre programme avec le fichier data.txt.

(a) Quel est le bénéfice optimal ?

* Le bénéfice optimal pour le fichier data.txt est de 21654.79332331

(b) Combien de produits différents faut-il fabriquer ?

*  Il faut fabriquer 6 produits différents

(c) Combien de temps a mis le solveur pour calculer la solution optimale ?

* Le solveur met moins d'une seconde pour calculer la soltion optimal

-----------------------------------------------------------

### Exercice 7:

Rajoutez les contraintes d’intégralité. Répondez aux questions de l’exercice
précédent. Expliquez le résultat.

(a) Quel est le bénéfice optimal ?

* Le bénéfice optimal pour le fichier data.txt est de 21638.0000

(b) Combien de produits différents faut-il fabriquer ?

* Il faut fabriquer 12 produits différents

(c) Combien de temps a mis le solveur pour calculer la solution optimale ?

* Le solveur met environs 20 secondes pour calculer la soltion optimal

-----------------------------------------------------------

### Exercice 8:

Essayez maintenant avec le fichier (beaucoup) plus volumineux bigdata.txt,
sans et avec les contraintes d’intégralité. Expliquez le résultat.

1) Sans les contraintes

(a) Quel est le bénéfice optimal ?

* Le bénéfice optimal pour le fichier bigdata.txt est de 5050533.10609334

(b) Combien de produits différents faut-il fabriquer ?

*  Il faut fabriquer 97 produits différents

(c) Combien de temps a mis le solveur pour calculer la solution optimale ?

* Le solveur met moins d'une seconde pour calculer la soltion optimal


2) Avec les contraintes

(a) Quel est le bénéfice optimal ?

* ?

(b) Combien de produits différents faut-il fabriquer ?

* ?

(c) Combien de temps a mis le solveur pour calculer la solution optimale ?

* ?

On remarque que le solveur avec les contraintes ne réponds pas (renvoie aucune solutions) dans un temps raisonnble.

-----------------------------------------------------------

## 3. Un problème de découpe

-----------------------------------------------------------

### Exercice 9:

Reprenez l’éxercice 4 de la feuille de TD 2 sur la d´ecoupe de barres
d’aluminium et trouvez la solution optimale avec le solveur. Comment faut-il découper les
barres de 3m pour minimiser le nombre utilisé ?

* D'après l'exercice 4 de la feuille TD2, le solveur nous trouve comme solutions:
  * Il faut au total 135 barre, soit 20 en 6 morceaux de 0.5m, 65 en 2 morceaux de 0.5m et 2 morceaux de 1m
  ainsi que 50 en 1 morceau de 0,5m et 2 morceux de 1,2m.

-----------------------------------------------------------

### Exercice 10:

Ecrivez une fonction qui prend en argument la longueur des barres de ´
base (en cm) ainsi qu’une liste de longueurs souhait´ees. La fonction génére tous les diff´erents
d´ecoupages maximaux possibles.

Par exemple, avec les entrées 300 et [120, 100, 50] comme dans l’exercice précédent, la
fonction utilise 0, 1 ou 2 éléments de longueur 120 et continue de fa¸con récursive avec les
éléments de longueurs 100 et ensuite 50. Pour que les d´ecoupages soient maximaux,
il faut toujours placer la plus petite longueur `a la fin et en prendre le maximum
possible.

* Le programme permettant d'éffectuer cette question est dans le fichier exerice10.py

-----------------------------------------------------------
