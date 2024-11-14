def cargar_existencias(filas, columnas):
    existencias =  []
    contador = 1  # Carga secuencial de camisetas
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(contador)
            contador += 1
        existencias.append(fila)
    return existencias

def calcular_totales(matriz, por_la_fila = True):
    totales = []
    if por_la_fila:
        for fila in matriz:
            total_fila = 0
            for elemento in fila:
                total_fila += elemento
                totales.append(total_fila)
    else:
        columnas = len(matriz[0])
        for j in range(columnas):
            total_columna = 0
            for i in range(len(matriz)):
                total_columna += matriz[i][j]
            totales.append(total_columna)
    return totales

def estimar_stock(totales, nombres, limite):
    excedidos = []
    i = 0
    while i < len(totales):
        if totales[i] > limite:
            excedidos.append(nombres[i])
        i += 1
    return excedidos

def obtener_maximo_por_equipo(matriz, equipos, depositos):
    maximos_por_equipo = []
    for j in range(len(equipos)): #recorre cada equipo por columna
        maxima_cantidad = matriz[0][j]
        maxima_deposito = depositos[0]
        for i in range(1, len(matriz)): #recorre cada deposito por fila
            if matriz[i][j] > maxima_cantidad:
                maxima_cantidad = matriz[i][j]
                maxima_deposito = depositos[i]
        maximos_por_equipo.append((equipos[j], maxima_cantidad, maxima_deposito))
    return maximos_por_equipo

