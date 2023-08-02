#Ejercicios sesion 4 estructuras selectivas
#Alejandro Villalobos Anguiano
#fecha de entrega 26/05/2023
H1 = int(input("hora actual: "))
if 0 <= H1 <= 23:
    H1=H1
    M1 = int(input("minuto actual: "))
    if 0 <= M1 <= 59:
       M1=M1
       H2= int(input("hora alarma: ")) 
       if 0 <= H2 <= 23:
        H2=H2
        M2 = int(input("minuto alarma: "))
        if 0 <= M2 <= 59:
            M2=M2
        
            total_minutos_actual = H1 * 60 + M1
            total_minutos_alarma = H2 * 60 + M2
            diferencia_minutos = total_minutos_alarma - total_minutos_actual

            if diferencia_minutos <= 0:
                diferencia_minutos += 24 * 60

            print("minutos descansados: ",diferencia_minutos)
            input("presione enter para salir ")
        else:
            print("Ingrese minutos correcto")
            input("presione enter para salir ")
    else:
        print("Ingrese minutos correcto")
        input("presione enter para salir ")
else:
    print("Ingrese una hora correcta")
    input("presione enter para salir ")
    

