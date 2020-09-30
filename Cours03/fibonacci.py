# initialiser des variables pour stocker deux termes de la suite
T1 = 1
T2 = 1

# initialiser un compteur
compteur = 0

# afficher un certain nombre de termes de la suite
while compteur < 10:
    print(T2, end=" ")

    T1, T2 = T2, T1 + T2
    compteur = compteur + 1
