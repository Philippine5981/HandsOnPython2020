# Définition d'une fonction "hello, world".
def hello(nom):
    chaine = "Bonjour"
    
    return chaine + " " + nom

# Définition d'une fonction qui calcule le cube d'un nombre passé en paramètre.
def cube(nombre):
    return nombre * nombre * nombre

# Définition d'une fonction qui affiche une table de multiplication par x.
def table(x):
    n = 1
    while n < 11:
        print(n * x, end='\t')
        n = n + 1
    print()

# Définition d'une fonction qui affiche successivement toutes les tables de multiplication entre
# mini et maxi, en utilisant la fonction précédente.
def tables(mini, maxi):    
    for i in range(mini, maxi+1):
        résultat = table(i)

# Définition d'une fonction testant la parité d'un entier.
def parité(x):
    if x % 2:
        return False
    else:
        return True


# À cet endroit du code, il ne s'est encore rien passé de concrêt, nous n'avons fait que "définir" les fonctions sans les utiliser.
# Maintenant, nous allons les appeler.
print(hello('jean'))
print(cube(2))
print(cube(3))

# Les fonctions "table(s)" ont été écrites avec des "print", ce qui n'est pas une bonne pratique (il vaut mieux "renvoyer" une valeur
# avec return et l'afficher à l'endroit de l'appel). Cependant, nous n'avons pas encore à disposition les types permettant de
# stocker des listes d'éléments, nous ferons évoluer ce code à ce moment.
table(7)
tables(3, 6)

# Testons la parité des multiples de 3 ...
for i in range(0, 30, 3):
    if parité(i):
        print(i, 'est pair')
    else:
        print(i, 'est impair')
        