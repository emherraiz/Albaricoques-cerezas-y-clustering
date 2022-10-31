from aprendizaje_no_supervisado_bueno import Aprendizaje
from generacion_de_datos_buena import generar_datos
import helpers
import pandas as pd

def menu():
    print("========================")
    print(" BIENVENIDO AL MENU ")
    print("========================")
    print("[1] Aprendizaje ")
    print("[2] Visualizacion 3D ")
    print("[3] Salir ")
    print("========================")

def iniciar():
    dtf=generar_datos()
    dtf.to_csv("frutas.csv", index=False,header=False)
    sdf = Aprendizaje('frutas.csv')

    while True:

        menu()
        opcion = int(input("> "))
        helpers.limpiar_pantalla()

        if opcion == 1:
            sdf.aprendizaje_gmm()

        if opcion == 2:
            sdf.visualizacion_3D()

        if opcion == 3:
            print("Saliendo...\n")
            break