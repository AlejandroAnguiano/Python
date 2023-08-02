#03/06/2023
#Alejandro Villalobos Anguiano
#Fernando Rene Moran Garcia

N = int(input("Ingrese cuantos anios dejara su inversion "))
while N < 1:
    N = int(input("Ingrese cuantos anios dejara su inversion(el numero debera ser mayor a 0) "))


M = int(input("Ingrese de cuanto sera su monto inicial "))
while M < 1:
    M = int(input("Ingrese de cuanto sera su monto inicial(el monto debera ser mayor a 0) "))
tasas = [3,3.5,4,4.5,5]
for i in tasas:
    print(f"Tasa: {i}%")
    tasita = M
    for j in range(1,N + 1):
        tasita = tasita *(1 + i/100)
        print(f"Anio {j}, monto = ${tasita:.3f}")

