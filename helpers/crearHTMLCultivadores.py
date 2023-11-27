import pandas as pd
from bs4 import BeautifulSoup
def crearTablaCultivadores(dataframeCultivadores,nombre):

    archivoHTML=dataframeCultivadores.to_html()
    rutaArchivo=f"tables/{nombre}.html"


    encabezado=''' 

    <!DOCTYPE html>
    <html lang="en">
    <head>
        <base href="../">
		<meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=0">
        <meta name="description" content="POS - Bootstrap Admin Template">
		<meta name="keywords" content="admin, estimates, bootstrap, business, corporate, creative, invoice, html5, responsive, Projects">
        <meta name="author" content="Dreamguys - Bootstrap Admin Template">
        <meta name="robots" content="noindex, nofollow">
        <title>Dreams Pos admin template</title>
        <link rel="shortcut icon" type="image/x-icon" href="images/ilustracion-diseno-logotipo-arbol-abstracto_43582-134.avif">
        <link rel="stylesheet" href="assets/css/bootstrap.min.css">
		<link rel="stylesheet" href="assets/css/bootstrap-datetimepicker.min.css">
        <link rel="stylesheet" href="assets/css/animate.css">
		<link rel="stylesheet" href="assets/plugins/select2/css/select2.min.css">
		<link rel="stylesheet" href="assets/css/dataTables.bootstrap4.min.css">
		<link rel="stylesheet" href="assets/plugins/fontawesome/css/fontawesome.min.css">
		<link rel="stylesheet" href="assets/plugins/fontawesome/css/all.min.css">
        <link rel="stylesheet" href="assets/css/style.css">
    </head>
    </html>
        '''


    sopa=BeautifulSoup(archivoHTML,'html.parser')

    for tr in sopa.find_all('tr'):
        tr.attrs.pop('style',None)

    archivoHTML=str(sopa) 
    archivoHTML=archivoHTML.replace('<table border="1" class="dataframe">','<table class="table table-striped">')

    with open(rutaArchivo,"w") as archivo:
        archivo.write(f"{encabezado}\n{archivoHTML}\n<body>\n<html>")