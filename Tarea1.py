#Ejercicios sesión 2. Salida con formato y operaciones numéricas.
#Alejandro Villalobos Anguiano
#fecha de entrega 22/05/2023

#Realiza un programa que solicite 5 registros completos de registros
#contables de los egresos mensuales de una persona.

nom = input ("ingresa tu presioso nombre: ")
ape= input ("ingresa tu hermosos apellido: ")

print("campo 1")
id0 = int(input ("ingresa el ID del producto: "))
desc0= str(input ("ingresa la descripcion del producto: "))
mon0 = float(input ("ingresa el monto total del producto: "))

print("campo 2")
id1 = int(input ("ingresa el ID del producto: "))
desc1=str(input ("ingresa la descripcion del producto: "))
mon1 = float(input ("ingresa el monto total del producto: "))

print("campo 3")
id2 = int(input ("ingresa el ID del producto: "))
desc2=str(input ("ingresa la descripcion del producto: "))
mon2 = float(input ("ingresa el monto total del producto: "))

print("campo 4")
id3= int(input ("ingresa el ID del producto: "))
desc3=str(input ("ingresa la descripcion del producto: "))
mon3 = float(input ("ingresa el monto total del producto: "))

print("campo 5")
id4 = int(input ("ingresa el ID del producto: "))
desc4=str(input ("ingresa la descripcion del producto: "))
mon4 = float(input ("ingresa el monto total del producto: "))

input ("Presione enter para ver el informe")
id= "ID"
desc= "Descripcion"
mon= "Monto"
tot="total"
acum=mon0
acum1=mon1+acum
acum2=mon2+acum1
acum3=mon3+acum2
acum4=mon4+acum3
print("detalles del informe")
print("registros de egresos de :{} {}".format(nom,ape))
print("{:5}-{:30}---{:10}--{:10}".format(id,desc,mon,tot))
print("{:5}-{:30}---{:10}--{:.2f}".format(id0,desc0,mon0,acum))
print("{:5}-{:30}---{:10}--{:.2f}".format(id1,desc1,mon1,acum1))
print("{:5}-{:30}---{:10}--{:.2f}".format(id2,desc2,mon2,acum2))
print("{:5}-{:30}---{:10}--{:.2f}".format(id3,desc3,mon3,acum3))
print("{:5}-{:30}---{:10}--{:.2f}".format(id4,desc4,mon4,acum4))