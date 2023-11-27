import csv

def crearCSVArboles(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['id_arbol','Nombre','Precio'])
        writer.writerows(lista)