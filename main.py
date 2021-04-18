import facteurs as ft

while True:
        try:
            nombre=int(input("Entrer une valeur  :\t"))
            break
        except:
            print("Veuillez entrer un nombre !")

ft.facteurs(nombre)
