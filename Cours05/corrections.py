
# Écrire une fonction qui calcule le maximum de trois entiers.
def maximum(a, b, c):
    # Est-ce que a est le maximum ?
    if a >= b and a >= c:
        return a
    
    # Sinon, est-ce b ? (plus besoin de tester a, puisqu'on sait déjà que ce n'est pas le maximum)
    if b >= c:
        return b
    
    # Sinon, c'est c (on sait déjà que ce n'est ni a, ni b)
    return c


# Écrire une fonction qui pour un numéro de mois donné renvoie le nom du mois associé.

# On initialise un tuple de portée globale au programme, car les noms de mois ne changeront jamais.
# Pas besoin donc de créer cette variable localement dans la fonction, car sa valeur ne dépendra jamais
# des paramètres d'entrée de la fonction.
liste_mois = ( "Janvier", "Février", "Mars", "Avril", "Mai", "Juin",
               "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre" )
    
def nom_mois(nb):
    # On vérifie que l'entrée ne soit pas en dehors de l'intervalle autorisée
    if nb < 1 or nb > 12:
        raise ValueError('Le numéro de mois est invalide.')
    
    # On renvoie le nom du mois en accédant à l'index (j'ai fait une erreur en cours, il faut bien
    # utiliser le numéro de mois auquel on retranche 1).
    return liste_mois[nb-1]


# Demandons à l'utilisateur une valeur de manière interactive.
while True:
    # On essaie de calculer le mois ...
    try:
        mois = nom_mois(int(input('Numéro de mois ? ')))
        print('Il s\'agit de', mois)
    # S'il y a une erreur, on sort de la bouble while avec l'instruction "break"
    except:
        break
        
    
# Fonction vérifiant si les trois dimensions fournies forment un triangle rectangle
def triangle_rectangle(a, b, c):
    # Tant que a n'est pas le maximum (l'hypothénuse potentielle), on effectue une rotation entre les trois valeurs.
    while maximum(a, b, c) != a:
        a, b, c = b, c, a
    
    # On teste si cet ordonancement satisfait le théorème de Pythagore et on renvoie le résultat
    return a**2 == b**2 + c**2


# Fonction d'interraction avec l'utilisateur
def boucle():
    terminé = False
    while not terminé:
        a = int(input('a ? '))
        b = int(input('b ? '))
        c = int(input('c ? '))
        
        if triangle_rectangle(a, b, c):
            print("C'est un triangle rectangle")
        else:
            print("Ce n'est pas un triangle rectangle")
        
        if input('Voulez vous continuer ? (oui/non)').lower().strip() != 'oui':
            terminé = True

# on appelle la boucle
boucle()

