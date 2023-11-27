from data.listaRefrigerios import refrigerios

from helpers.crearHTMLRefrigerios import crearTablaRefrigerios
from helpers.crearCSVRefrigerios import crearCSVRefrigerios

import pandas as pd

crearCSVRefrigerios(refrigerios,'bdRefrigerios.csv')

#creando un dataframe desde una fuente CSV
dataFrameRefrigerios=pd.read_csv('data/bdRefrigerios.csv')


#convertir el DF en TABLA HTML
crearTablaRefrigerios(dataFrameRefrigerios,'refrigerios')

