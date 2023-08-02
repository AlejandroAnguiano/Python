#03/06/2023
# Fernando Rene Moran Garcia
#Alejandro Villalobos Anguiano

N=int(input("ingrese su valor N: "))
M=int(input("ingrese su valor M: "))

while  N > M:
    print("Rango invalido (recuerde que N debe ser menor que M y bien pendejo)")
    N=int(input("ingrese su valor N: "))
    M=int(input("ingrese su valor M: "))

for i in range(N,M+1):
    for j in range (1,11):
        result= j * i
        print (f"Resultado de {i} X {j} = {result}")
    input("presione enter para continuar")
