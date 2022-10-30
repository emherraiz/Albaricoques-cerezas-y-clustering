import pandas as pd
import matplotlib.pyplot as plt

#---- Modelo de K-Mean (K-Medias)-----------
# Para cantidades pequeñas de datos (inferior a 10.000)
from sklearn.cluster import KMeans

#---- Modelo de mezclas Gaussianas (GMM) -----------
from sklearn import mixture

# Para guardar nuestro modelo en un fichero
from joblib import dump

class Aprendizaje():

    def __init__(self, name_df):
        '''_summary_: Constructor de la clase Aprendizaje

        Args:
            name_df (str): Nombre del fichero csv que contiene los datos de las frutas
        '''
        self.frutas = pd.read_csv(name_df, names=['DIAMETRO','PESO'], header=None)
        self.modelo = None
        self.predicciones = None

    def aprendizaje_KMeans(self, n_clusters = 2):
        '''_summary_: Aprendizaje no supervisado con el algoritmo K-Means

        Args:
            n_clusters (int, optional): Número de clusters. Defaults to 2.
        '''
        # Utilizamos 2 clusters por defecto en el modelo.
        self.modelo = KMeans(n_clusters)

        # Ajustamos el modelo con nuestro DataFrame
        self.modelo.fit(self.frutas)

        # Predicciones
        self.predicciones = self.modelo.predict(self.frutas)

    def aprendizaje_gmm(self, n_componentes = 2):
        '''_summary_: Aprendizaje no supervisado con el algoritmo GMM

        Args:
            n_componentes (int, optional): Número de componentes. Defaults to 2.'''

        # Utilizamos 2 clusters por defecto en el modelo.
        self.modelo = mixture.GaussianMixture(n_components = n_componentes)

        # Ajustamos el modelo con nuestro DataFrame
        self.modelo.fit(self.frutas)

        # Predicciones
        self.predicciones = self.modelo.predict(self.frutas)

    def predecir_fruta(self, diametro, peso):
        '''_summary_: Predice a que cluster pertenece una fruta

        Args:
            diametro (float): Diametro de la fruta
            peso (float): Peso de la fruta

        Returns:
            int: Cluster al que pertenece la fruta
        '''
        return self.modelo.predict([[diametro, peso]])



    def visualizacion(self):
        '''_summary_: Visualización de los datos y de la clusterización'''

        # Visualización gráfica de los datos
        # x = Diametro
        # y = peso
        # c = lista o matriz que asigna colores a cada uno de las frutas
        #   NOTA: En caso de pasarle un string con el nombre del color imprime todas las frutas del mismo color
        # s = Tamaño de las frutas en la gráfica
        # cmap = Secuencia de colores que vamos a seguir
        # Referencia de colores https://matplotlib.org/2.0.2/examples/color/colormaps_reference.html
        plt.scatter(self.frutas.DIAMETRO, self.frutas.PESO, c = self.predicciones, s = 30, cmap = 'viridis')

        # Etiqueta eje x
        plt.xlabel("DIAMETRO")

        # Etiqueta eje y
        plt.ylabel("PESO")

        if type(self.modelo) == KMeans:
            # Visualización de los centroides
            centers = self.modelo.cluster_centers_
            plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)

        # Mostramos la gráfica
        plt.show()

    def guardar_modelo(self, name_model):
        '''_summary_: Guarda el modelo en un fichero

        Args:
            name_model (str): Nombre del fichero donde se va a guardar el modelo
        '''
        dump(self.modelo, name_model)






