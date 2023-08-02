datos = []

def capturar_datos():
    while True:
        dato = input("Dame valor numérico, o solo ENTER para terminar la captura: ").strip()
        if dato == "":
            break
        #endif
        datos.append(eval(dato))
    #endwhile
#enddef

def promediar():
    #función que regrese el promedio
    d = len(datos)
    #a = sum(datos)
    a = 0 #acumulador de los datos de la variable datos
    for x in datos:
        a = a + x
    #endfor
    return a/d

def obtener_moda():
    #esta función regresa el valor moda, o la palabra "no hay moda" en caso que ningún valor se repita
    max_repeticiones =0
    valor_moda = 0
    for i in range(len(datos)):
        veces = datos.count(datos[i])
        if max_repeticiones < veces:
            max_repeticiones = veces
            valor_moda = datos[i]
        #endif
    #endfor
    if max_repeticiones == 1:
        return "no hay moda"
    else:
        return valor_moda
#enddef

#mediana es el valor centra en un conjunto de datos ordenados
#[8,9,9,10,10,10] , como son cantidad de valores pares, promedio los centrales: 9.5
#[6,7,7,8,9], la mediana: 7
#cuidado de ordenar los valores antes de calcular la mediana
def obtener_mediana():
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    return mediana

#enddef

#aplicar la fórmula, que estará en la documentación y en el chat de teams.
def obtener_desviacion_estandar():
    d = len(datos)
    a = 0 #acumulador de los datos de la variable datos
    for x in datos:
        a = a + x
    #endfor
    promedio = a/d
    suma_cuadrados = sum((dato - promedio)**2 for dato in datos)
    varianza = suma_cuadrados / len(datos)
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar
#enddef

