from data.ListaCultivadores import cultivadores
from helpers.crearCSVCultivadores import crearCSVCultivadores
from helpers.crearHTMLCultivadores import crearTablaCultivadores

import pandas as pd

crearCSVCultivadores(cultivadores,'bdCultivadores.csv')

#creando un dataframe desde una fuente CSV
dataFrameCultivadores=pd.read_csv('data/bdCultivadores.csv')


#convertir el DF en TABLA HTML
crearTablaCultivadores(dataFrameCultivadores,'cultivadores')

filtroUno=dataFrameCultivadores.query("(Edad<30) and (Nombre=='Juan')")
print(filtroUno)