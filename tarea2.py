#03/06/2023
#Fernando Rene Moran Garcia
#Alejandro Villalobos Anguiano
import random
a=["piedra","papel","tijera"]
print("1 significa piedra, 2 significa papel,3 significa tijeras")

acumM=0
acumU=0
jugar= 0
partidas=0

while  jugar==0:
    U= int (input("Seleccione su jugada: "))
    while U > 3 or U < 1:
        U= int (input("Seleccione una jugada valida (del 1 al 3 ): "))
    M= random.randint(1,3)
    if (U==M):
        print("Empate nadie gana")
        partidas+=1
    elif (U==1):
        if (M==2):
            print("perdiste ")
            acumM+=1
            partidas+=1
        else :
            print("ganaste ")
            acumU+=1
            partidas+=1
    elif (U==2):
        if (M==3):
            print("perdiste ")
            acumM+=1
            partidas+=1
        else :
            
            print("ganaste ")
            acumU+=1
            partidas+=1
    elif (U==3):
        if (M==1):
            print("perdiste ")
            acumM+=1
            partidas+=1
        else :
            print("ganaste ")
            acumU+=1
            partidas+=1

    print("Usted escogio ",a[U-1])
    print("Su rival escogio ", a[M-1])

    jugar=int(input("desea seguir jugando? presione 0 para continuar, si no, presione otro numero: "))

print(f"Numero de partidas jugadas: {partidas},ganadas: {acumU},perdidas: {acumM},empatadas {partidas-(acumM+acumU)}")
    
            
        
        
