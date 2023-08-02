'''
Para poder traducir de las instrucciones en ensamblador a codigo en hexadecimal se opto por programar 
un traductor que nos entregara la instruccion lista para la memoria de instrucciones

Programado por Alejandro Villaobos Y Rene Garcia 
"todo los derechos reservados"
'''
table_R = {
    'ADD':  '000000',
    'STL':  '000001',
    'AND':  '000010',
    'OR':   '000011',
    'SUB':  '000100',
    'NOR':  '000101',  
}
table_I ={
    'ADDI': '000110',
    'ORI':  '001001',
    'BEQ':  '001010',
}
table_i2={
    'LW':   '000111',
    'SW':   '001000'
}
table_J ={'JMP':  '001011'}


def convertir_valores(v1, v2, v3):
    # Convertir a binario
    valor1 = int(v1)
    valor2 = int(v2)
    valor3 = int(v3)
    a = format(valor1, "05b")
    b = format(valor2, "05b")
    c = format(valor3, "05b")
    return a, b, c
def convertir_valores1(v1, v2, v3):
    # Convertir a binario
    valor1 = int(v1)
    valor2 = int(v2)
    valor3 = int(v3)
    a = format(valor1, "05b")
    b = format(valor2, "05b")
    c = format(valor3, "05b").zfill(16)
    return a, b, c
def convertir_valores2(v1):
    # Convertir a binario
    valor1 = int(v1)

    a = format(valor1, "05b").zfill(26)
    
    return a

def binario_a_hexadecimal(binario):
    decimal = int(binario, 2)
    hexadecimal = hex(decimal)[2:]
    return hexadecimal.upper()

val = int(input("Ingrese cuantos valores quiere: "))

for i in range(val):
    entrada = input("Ingrese la instruccion: ")
    palabras = entrada.split()
    com = palabras[0].upper()
    if com in table_R:
        R_type = entrada.replace("$", " ").replace(",", " ") 
        R_type1=R_type.split()
        conv=convertir_valores(R_type1[2], R_type1[3], R_type1[1])
        if com == "ADD":
            bin1=str("000000"+conv[0]+conv[1]+conv[2]+"00000100000")
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1)  
        if com == "STL":
            bin1=str("000000"+conv[0]+conv[1]+conv[2]+"00000101010")
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1) 
        if com == "AND":
            bin1=str("000000"+conv[0]+conv[1]+conv[2]+"00000100100")
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1) 
        if com == "OR":
            bin1=str("000000"+conv[0]+conv[1]+conv[2]+"00000100101")
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1) 
        if com == "SUB":
            bin1=str("000000"+conv[0]+conv[1]+conv[2]+"00000100010")
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1) 
        if com == "NOR":
            bin1=str("000000"+conv[0]+conv[1]+conv[2]+"00000100111")
            print(bin1)
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1) 
    if com in table_I:
        I_type = entrada.replace("$", " ").replace(",", " ").replace("(", " ").replace(")", "") 
        I_type1 = I_type.split()
        I_type1 = [elem.strip() for elem in I_type1] 
        conv = convertir_valores1(I_type1[2], I_type1[1], I_type1[3])
        conv1 = (conv[2]).zfill(16)
        total=(conv[0],conv[1],conv1)
        if com == "ADDI":
            bin1=str("001000"+total[0]+total[1]+total[2])
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                hexa1=hexa1.zfill(8)
                print("Codigo:",hexa1)
            else:
              print("Codigo:",hexa1) 
        
        if com == "ORI":
            bin1=str("001101"+total[0]+total[1]+total[2])
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                 hexa1=hexa1.zfill(8)
                 print("Codigo:",hexa1)
            else:
                print("Codigo:",hexa1) 
        if com == "BEQ":
            bin1=str("000100"+total[0]+total[1]+total[2])
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                 hexa1=hexa1.zfill(8)
                 print("Codigo:",hexa1)
            else:
                print("Codigo:",hexa1) 
    if com in table_i2:
        I_type = entrada.replace("$", " ").replace(",", " ").replace("(", " ").replace(")", "") 
        I_type1 = I_type.split()
        I_type1 = [elem.strip() for elem in I_type1] 
        conv = convertir_valores1(I_type1[3], I_type1[1], I_type1[2])
        conv1 = (conv[2]).zfill(16)
        total=(conv[0],conv[1],conv1)   
        if com == "SW":
            bin1=str("101011"+total[0]+total[1]+total[2])
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                 hexa1=hexa1.zfill(8)
                 print("Codigo:",hexa1)
            else:
                print("Codigo:",hexa1) 
        if com == "LW":
            bin1=str("100011"+total[0]+total[1]+total[2])
            print(bin1, total)
            hexa1=binario_a_hexadecimal(bin1)
            if len(hexa1) < 8:
                 hexa1=hexa1.zfill(8)
                 print("Codigo:",hexa1)
            else:
                print("Codigo:",hexa1) 
    if com in table_J:
        J_type = entrada
        J_type1 = J_type.split() 
        conv_j=convertir_valores2(J_type1[1]) 
        bin1=str("000010"+conv_j)
        hexa1=binario_a_hexadecimal(bin1)
        if len(hexa1) < 8:
                 hexa1=hexa1.zfill(8)
                 print("Codigo:",hexa1)
        else:
                print("Codigo:",hexa1) 

