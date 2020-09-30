# définition des constantes, ce sera plus simple d'utiliser des noms plutôt que des nombres
MINUTE = 60
HEURE = MINUTE * 60
JOUR = HEURE * 24

# valeur initiale
secondes = 86466 + 3600

# on sépare en jours et secondes restantes
jours = secondes // JOUR
secondes = secondes % JOUR

# s'il y a au moins un jour, on affiche les jours
if jours > 0:
    print(jours, "jours")

# on affiche les secondes restantes
print("il reste", secondes, "secondes")

# même principe avec les heures
heures = secondes // HEURE
secondes = secondes % HEURE
if heures > 0:
    print(heures, "heures")
print("il reste", secondes, "secondes")
