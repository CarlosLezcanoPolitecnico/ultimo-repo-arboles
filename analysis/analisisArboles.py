from data.ListaArboles import arboles
from helpers.crearCSV import crearCSVArboles
from helpers.crearHTML import crearTabla

import pandas as pd



crearCSVArboles(arboles,'bdArboles.csv')

#creando un dataframe desde una fuente CSV
dataFrameArboles=pd.read_csv('data/bdArboles.csv')

#convertir el DF en TABLA HTML
crearTabla(dataFrameArboles,'arboles')


