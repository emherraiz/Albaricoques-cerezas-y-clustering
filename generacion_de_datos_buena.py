import random
import pandas as pd

def generar_datos():

    #---- CARACTERÍSTICAS------

    # CEREZAS:
        # Diametro minimo (mm)
        # Diametro maximo (mm)
        # Peso minimo (g)
        # Peso maximo (g)

    caracteristicasCerezas = [[17,19,1,5],[20,21,5,6],[22,23,6,7],[24,25,7,8.5],[26,27,8.5,10],[28,29,10,11.5]]

    #ALBARICOQUES: ATENCIÓN DOS CASOS DE PRUEBAS EN FUNCIÓN DEL AVANCE DE SU LECTURA
    # Diametro minimo (mm)
    # Diametro maximo (mm)
    # Peso medio (g)
    caracteristicasAlbaricoques = [[40,44,41],[45,49,54],[50,54,74],[55,59,100]]

    # Cantidad de observaciones
    n = 200

    # Semilla
    random.seed()

    #Generación de las cerezas
    cerezas = []
    random.seed()
    for iteration in range(n):
        # random.choice(): Elección al azar de una característica
        cereza = random.choice(caracteristicasCerezas)

        # Generación de un diámetro
        # random.uniform(a, b): Valor aleatorio entre a y b
        # Todos los valores son igual de probables dentro del intervalo
        diametro = round(random.uniform(cereza[0], cereza[1]), 2)

        # Generación de un peso
        peso = round(random.uniform(cereza[2], cereza[3]), 2)
        #print ("Cereza "+str(iteration)+" "+str(cereza)+" : "+str(diametro)+" - "+str(peso))

        # Añadimos a la lista de cerezas el diametro y el peso de cada una de ellas
        cerezas.append([diametro, peso])

    # Generación de los albaricoques
    # Similar a como hicimos con las cerezas
    albaricoques = []
    random.seed()
    for iteration in range(n):
        # Elección al azar de una característica
        albaricoque = random.choice(caracteristicasAlbaricoques)

        # Generación de un diámetro
        diametro = round(random.uniform(albaricoque[0], albaricoque[1]), 2)

        # Generación de un peso
        # El limite minimo y maximo de peso lo ponemos dividiendo y multiplicando por un valor respectivamente
        # De esta manera el peso medio siempre va a ser el mismo
        # Es aconsejable que este numero no sea muy grande para que los limites no difieran mucho de la realidad
        # En este caso es un 10%
        limiteMinPeso = albaricoque[2] / 1.10
        limiteMaxPeso = albaricoque[2] * 1.10
        peso = round(random.uniform(limiteMinPeso, limiteMaxPeso), 2)
        #print ("Albaricoque "+str(iteration)+" "+str(albaricoque)+" : "+str(diametro)+" - "+str(peso))

        # Añadimos a la lista de albaricoques el diametro y el peso de cada una de ellos
        albaricoques.append([diametro,peso])

    # NOTA: Sería mas óptimo meter los dos bucles for en uno solo


    #Constitución de las observaciones
    # Concatenamos en una lista las observaciones de cerezas y albaricoques
        frutas = cerezas+albaricoques
        print(frutas)

    # De seguido mezclamos la lista al azar, de esta manera no sabremos donde se encuentra cada fruta
        random.shuffle(frutas)

    # Guardado de las observaciones en un archivo
        dataFrame = pd.DataFrame(frutas)
        return dataFrame





