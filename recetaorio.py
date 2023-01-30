from os import system, name, listdir
from pathlib import Path


def recetario():
    valid = False
    while not valid:
        clear()
        
        print("""Elija una de las siguientes opciones:
        [1] Leer receta
        [2] Crear receta
        [4] Eliminar receta
        [5] Eliminar categoría
        [6] Finalizar programa""")

        option = input()
        match option:
            case "1":
                option1()
                print("La opción 1 le va a preguntar qué categoría elige (carnes, ensaladas, etc.), y una vez que el usuario elija una, le va a preguntar qué receta quiere leer, y mostrar su contenido.")
            case "2":
                print("En la opción 2 también se le va a hacer elegir una categoría, pero luego le va a pedir que escriba el nombre y el contenido de la nueva receta que quiere crear, y el programa va a crear ese archivo en el lugar correcto")
            case "3":
                print("La opción 3 le va a preguntar el nombre de la categoría que quiere crear y va a generar una carpeta nueva con ese nombre.")
            case "4":
                print("La opción 4, hará todo lo mismo que la opción uno, pero en vez de leer la receta, la va a eliminar")
            case "5":
                print("La opción 5, le va a preguntar qué categoría quiere eliminar")
                option5()
            case "6":
                print("Usted eligio salir del recetario")
                valid = True
            case _:
                print("No existe esta opcion")


def option1():
    clear()
    input(f"Elija una categoria ")
    recetario()

def option2():
    clear()
    recetario()

def option3():
    clear()
    recetario()

def option4():
    clear()
    recetario()

def option5():
    clear()
    input(f"Escriba la categoria que desea eliminar {listdir(Path.cwd())}")
    recetario()


def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
clear()
print(f" Bienvenido las recetas se encuentran en {Path.cwd()}")
input("De un enter para continuar")
recetario()