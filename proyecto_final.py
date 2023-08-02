#Alejandro Villalobos anguiano
# Fecha de entrega 19/06/2023
#Primero Hcemos un diccionario donde asociaremos el codigo con el nombre del producto
Maquina={
    'A1': 'M&M',
    'A2': 'MilkyWay',
    'A3': 'Barra Granola',
    'A4': 'Habaneras',
    'B1': 'Sabritas',
    'B2': 'Fritos',
    'B3': 'Sabritones',
    'B4': 'Ruffles',
    'C1': 'CocaCola',
    'C2': 'Fanta',
    'C3': 'Sidral',
    'C4': 'Agua Mineral'
}
#Crearemos un funcion que nos permita en base al dinero ingresado seleccionar un producto, saber cuanto saldo hay disponible y
#en caso de no tener suficiente saldo notificarlo, a su vez dar el cambio
def Conteo_De_Dinero(dinero_inicial):
    print('Ingrese el codigo del producto que desea:')
    dinero_actual = dinero_inicial
    contador_compras = 0
    
    while True:
        codigo = str(input().upper())
        
        if codigo == '0':
            break
        if codigo == 'A1':
            print(Maquina[codigo])
            precio = 14
        elif codigo == 'A2':
            precio = 14
            print(Maquina[codigo])
        elif codigo == 'A3':
            precio = 10
            print(Maquina[codigo])
        elif codigo == 'A4':
            precio = 8
            print(Maquina[codigo])
        elif codigo == 'B1':
            precio = 15
            print(Maquina[codigo])
        elif codigo == 'B2':
            precio = 12
            print(Maquina[codigo])
        elif codigo == 'B3':
            precio = 12
            print(Maquina[codigo])
        elif codigo == 'B4':
            precio = 13
            print(Maquina[codigo])
        elif codigo == 'C1':
            precio = 12
            print(Maquina[codigo])
        elif codigo == 'C2':
            precio = 10
            print(Maquina[codigo])
        elif codigo == 'C3':
            precio = 10
            print(Maquina[codigo])
        elif codigo == 'C4':
            precio = 10
            print(Maquina[codigo])
        else:
            print("Codigo invalido")
            continue
        
        if dinero_actual >= precio:
            dinero_actual -= precio
            contador_compras += 1
        else:
            print("Saldo Insuficiente")
            
        
        print('Su saldo actual es: $',dinero_actual)
    
    print('Productos adquiridos: ',contador_compras)
    print('Su cambio:$',dinero_actual,'Gracias vuelva pronto UwU')

#Finalmente iniciaremos el programa ingresando el dinero,imprimiendo el "Menu" , mandando a llamar a la funcion de conteo de dinero
dinero_inicial = int(input("Introduce la cantidad de dinero :$ "))
for clave, valor in Maquina.items():
    print(f"{clave}: {valor}")

Conteo_De_Dinero(dinero_inicial)
