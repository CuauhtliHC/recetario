from os import system, name, listdir, remove, rmdir, makedirs
from pathlib import Path

ruta = Path(Path.cwd(), 'Recetas')
listCategory =  sorted(listdir(ruta))
stringCategory = ", ".join(listCategory)
listLower = [x.lower() for x in listCategory]

def recetario():
    valid = False
    while not valid:
        clear()     
        print("""Elija una de las siguientes opciones:
        [1] Leer receta
        [2] Crear receta
        [3] Crear categoría
        [4] Eliminar receta
        [5] Eliminar categoría
        [6] Finalizar programa""")
        option = input()
        match option:
            case "1":
                option1()
                print("La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.")
            case "2":
                option2()
                print("En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va a crear ese archivo en el lugar correcto")
            case "3":
                option3()
            case "4":
                option4()
            case "5":
                option5()
            case "6":
                clear()
                valid = True
                print("Usted eligio salir del recetario")      
            case _:
                print("No existe esta opcion")


def option1():
    validCategory = False
    while not validCategory:
        clear()
        category = input(f"Escriba la categoria donde se encuentra la receta que desea leer: {stringCategory}: ")
        if category.lower() in listLower:
            rutaReceta = Path(ruta, category.lower().capitalize())
            listRecetas = sorted(listdir(rutaReceta))
            listWhitoutTxt = [x.replace(".txt", "") for x in listRecetas]
            stringRecetas = ", ".join(listWhitoutTxt)
            validCategory = True
            validReceta = False
            while not validReceta:
                receta = input(f"Que receta desea leer: {stringRecetas}: ")
                if receta.lower() in [x.lower() for x in listWhitoutTxt]:
                    indexReceta = [x.lower() for x in listWhitoutTxt].index(receta.lower())
                    fileReceta = open(Path(rutaReceta, listRecetas[indexReceta]))
                    print(fileReceta.read())
                    fileReceta.close()
                    input("Desea regresar")
                    validReceta = True
                else:
                    input("La receta que escogio no se encuentra de enter para escoger nuevamente")
        else:
            input("La categoria que escogio no se encuentra de enter para escoger nuevamente")

def option2():
    validCategory = False
    while not validCategory:
        clear()
        category = input(f"Escriba la categoria donde desea crear la receta: {stringCategory}: ")
        if category.lower() in listLower:
            rutaReceta = Path(ruta, category.lower().capitalize())
            listRecetas = sorted(listdir(rutaReceta))
            listWhitoutTxt = [x.replace(".txt", "") for x in listRecetas]
            validCategory = True
            validReceta = False
            while not validReceta:
                nameReceta = input("Escriba el nombre de la receta: ")                
                if nameReceta.lower() not in [x.lower() for x in listWhitoutTxt]:
                    contentReceta = input("Escriba su receta: ")
                    nameReceta = nameReceta.lower().capitalize() + ".txt"
                    fileReceta = open(Path(rutaReceta, nameReceta), "w")
                    fileReceta.write(contentReceta)
                    validReceta = True
                    input("Receta creada")
                else:
                    input("El nombre de la receta que escogio ya existe")
        else:
            input("La categoria que escogio no se encuentra de enter para escoger nuevamente")

def option3():
    validCategory = True
    while validCategory:
        clear()
        category = input(f"Escriba el nombre de la categoria que desea crear: ")
        if category.lower() not in listLower:
            validCategory = False
            makedirs(Path(ruta, category.lower().capitalize()))
            input(f"Se a creado la categoria {category.lower().capitalize()}")
        else:
            input("Esta categoria ya existe escoja otro nombre")


def option4():
    validCategory = False
    while not validCategory:
        clear()
        category = input(f"Escriba la categoria donde se encuentra la receta que desea eliminar {stringCategory}: ")
        if category.lower() in listLower:
            rutaReceta = Path(ruta, category.lower().capitalize())
            listRecetas = sorted(listdir(rutaReceta))
            listWhitoutTxt = [x.replace(".txt", "") for x in listRecetas]
            stringRecetas = ", ".join(listWhitoutTxt)
            validCategory = True
            validReceta = False
            while not validReceta:
                receta = input(f"Que receta desea eliminar {stringRecetas}: ")
                if receta.lower() in [x.lower() for x in listWhitoutTxt]:
                    indexReceta = [x.lower() for x in listWhitoutTxt].index(receta.lower())
                    input(f"Se eliminara la receta {listWhitoutTxt[indexReceta]}")
                    remove(Path(rutaReceta, listRecetas[indexReceta]))
                    validReceta = True
                else:
                    input("La receta que escogio no se encuentra de enter para escoger nuevamente")
        else:
            input("La categoria que escogio no se encuentra de enter para escoger nuevamente")

def option5():
    validCategory = False
    while not validCategory:
        clear()
        category = input(f"Escriba la categoria que desea eliminar {stringCategory}: ")
        if category.lower() in listLower:
            indexCategory = listLower.index(category.lower())
            print("Borrar directorio")
            rmdir(Path(ruta, listCategory[indexCategory]))
            validCategory = True
        else:
            input("La categoria que escogio no se encuentra de enter para escoger nuevamente")


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
clear()
print(f"Bienvenido las recetas se encuentran en {ruta}")
input("De un enter para continuar")
recetario()