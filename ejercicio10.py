def solicitar_datos():
    datos = []
    while True:
        dato = input("Ingrese un número (o 'q' para finalizar): ")
        if dato.lower() == 'q':
            break
        try:
            numero = float(dato)
            datos.append(numero)
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido o 'q' para finalizar.")
    return datos

def calcular_promedio(datos):
    total = sum(datos)
    promedio = total / len(datos)
    return promedio

def calcular_moda(datos):
    frecuencias = {}
    for dato in datos:
        frecuencias[dato] = frecuencias.get(dato, 0) + 1
    moda = [dato for dato, frecuencia in frecuencias.items() if frecuencia == max(frecuencias.values())]
    return moda

def calcular_mediana(datos):
    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    if n % 2 == 0:
        mediana = (datos_ordenados[n//2 - 1] + datos_ordenados[n//2]) / 2
    else:
        mediana = datos_ordenados[n//2]
    return mediana

def calcular_desviacion_estandar(datos):
    promedio = calcular_promedio(datos)
    suma_cuadrados = sum((dato - promedio)**2 for dato in datos)
    varianza = suma_cuadrados / len(datos)
    desviacion_estandar = varianza ** 0.5
    return desviacion_estandar

# Solicitar datos al usuario
print("Ingrese un conjunto de datos numéricos. Ingrese 'q' para finalizar.")

conjunto_datos = solicitar_datos()

if len(conjunto_datos) > 0:
    # Calcular promedio
    promedio = calcular_promedio(conjunto_datos)
    print("Promedio:", promedio)

    # Calcular moda
    moda = calcular_moda(conjunto_datos)
    print("Moda:", moda)

    # Calcular mediana
    mediana = calcular_mediana(conjunto_datos)
    print("Mediana:", mediana)

    # Calcular desviación estándar
    desviacion_estandar = calcular_desviacion_estandar(conjunto_datos)
    print("Desviación estándar:", desviacion_estandar)
else:
    print("No se ingresaron datos.")
