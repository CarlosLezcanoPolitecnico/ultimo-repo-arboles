import random
refrigerios=[]

for _ in range(2):
    precio=random.randint(5000,20000)
    nombre=random.choice(['Sandwich','Torta','Mecato','Empanada', 'Buñuelo'])
    cantidad=random.randint(18,60)
    costototal=precio * cantidad


    refrigerio=[precio, nombre, cantidad, costototal]
    refrigerios.append(refrigerio)

print(refrigerios)
