import csv

def crearCSVCultivadores(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Cedula','Nombre','Edad'])
        writer.writerows(lista)