#03/06/2023
#Alejandro Villalobos Anguiano
#Fernando Rene Moran Garcia
import random


frases_aleatorias = [
    "¡Sigue intentando, lo estás haciendo bien!",
    "¡No te rindas, estás cada vez más cerca!",
    "¡Vas por buen camino, sigue practicando!",
    "¡Excelente esfuerzo, sigue así!",
]

nombre = str(input("Ingrese su nombre profavor: "))
seguir = 0
puntuacion = 0
intentos = 0
acierto = True
historial = []
while seguir == 0:
    if acierto == True:
        numero1 = random.randint(1,99) 
        numero2 = random.randint(1,99)
        while numero1 < numero2:
            numero1 = random.randint(1,99) 
        acierto = False
    respuesta = int(input(f"Cuanto es {numero1} - {numero2} "))
    if(respuesta == (numero1 - numero2)):
        historial.append([numero1,numero2,respuesta,intentos])
        print(f"Felicidades {nombre}, lo lograste en {intentos} intentos")
        intentos = 0
        acierto = True
        puntuacion += 1
    else:
        intentos += 1
        motiv = random.randint(0,3)
        print(frases_aleatorias[motiv])
    seguir = int(input("Si deseas seguir restando ingresa 0 si ya no quieres restar ingresa otro numero "))

print(f"Felicidades {nombre}, lograste {puntuacion} puntos")
for i in range(puntuacion):
    print(historial[i][0],"-",historial[i][1],"=",historial[i][2]," numero de intentos: ",historial[i][3])
