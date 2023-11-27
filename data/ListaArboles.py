import random
arboles=[]

for _ in range(500):
    id_arbol=random.randint(1,3000)
    nombre=random.choice(['Ceiba','Guayaca','Caova','Quina', 'Laurel', 'Caucho'])
    precio=random.randint(1000,100000)

    arbol=[id_arbol, nombre, precio]
    arboles.append(arbol)

print(arboles)