frase = int(input("Ingrese cuantas palabras quieres"))
datos= list()
for i in range (frase):
   # frase1 = frase.replace(f"palabra{i+1}", palabras, 1)
    palabras = input().split("\n")
    datos.append(palabras)
for i in range (frase): 
    print("DUT.INSmemory.mem_array[{}] = 32'h{};".format(i,*datos[i]))
input("presione enter para salir ")
