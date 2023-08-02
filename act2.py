#Ejercicios sesion 4 estructuras selectivas
#Alejandro Villalobos Anguiano
#fecha de entrega 26/05/2023
import math

print("ingrese los tres puntos del triángulo : ")
x1= int(input("ingrese x1: "))
y1= int(input("ingrese y1: "))
x2= int(input("ingrese x2: "))
y2= int(input("ingrese y2: "))
x3= int(input("ingrese x3: "))
y3= int(input("ingrese y3: "))

dis1 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
dis2 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
dis3 = math.sqrt((x3 - x2)**2 + (y3 - y2)**2)
margen = 0.001

if abs(dis1 - dis2) < margen and abs(dis1 - dis3) < margen:
    triangulo = "equilatero"
elif abs(dis1 - dis2) < margen or abs(dis1 - dis3) < margen or abs(dis2 - dis3) < margen:
    triangulo = "isoceles"
else:
    triangulo = "escaleno"

print(triangulo)
