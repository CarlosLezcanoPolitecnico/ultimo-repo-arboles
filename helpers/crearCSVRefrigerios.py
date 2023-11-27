import csv

def crearCSVRefrigerios(lista,nombreArchivo):
    with open('data/'+nombreArchivo,mode='w',newline='',encoding='utf-8')as archivoCSV:
        writer=csv.writer(archivoCSV)
        writer.writerow(['Precio','Nombre','Cantidad', 'Costo Total'])
        writer.writerows(lista)