import funciones_estadisticos as fe

if __name__ == "__main__":
    fe.capturar_datos()
    print(fe.datos)
    prom = fe.promediar()
    print("Promedio: ",prom)
    moda = fe.obtener_moda()
    print("Moda: ",moda)
    mediana = fe.obtener_mediana()
    print("Mediana:", mediana)
    desviacion_estandar = fe.obtener_desviacion_estandar()
    print("Desviacion estándar:", desviacion_estandar)
#endif principal