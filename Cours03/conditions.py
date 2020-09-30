# demander un nombre à l'utilisateur
nombre = int(input("nombre ?"))

# afficher quelques petits calculs
print("nombre % 2 =", nombre % 2)
print("bool(nombre % 2) =", bool(nombre % 2))

# tester si le nomre est pair ou impair, et en informer l'utilisateur
if nombre % 2:
    print(nombre, "est impair.")
else:
    print(nombre, "est pair.")
