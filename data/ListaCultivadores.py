import random
cultivadores=[]

for _ in range(50):
    cedula=random.randint(43000000,120403304)
    nombre=random.choice(['Carlos','Esteban','Catta','Julian', 'Juan', 'Pablo'])
    edad=random.randint(18,60)

    cultivador=[cedula, nombre, edad]
    cultivadores.append(cultivador)

print(cultivadores)