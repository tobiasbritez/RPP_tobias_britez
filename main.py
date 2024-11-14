"""
Ejercicio 1:
Se debe modularizar correctamente, utilizar parámetros opcionales y cumplir reglas de estilo.
No puede haber código repetido, ni funciones que realicen múltiples tareas. No se puede
utilizar sets, diccionarios, ni tuplas.
Una empresa se dedica al almacenamiento y posterior distribución de camisetas de fútbol en
todo el país. Para ello cuentan con 6 depósitos: Tierra del Fuego, Tucumán, Mendoza, Bs
As, Misiones y Santa Fé.
Los depósitos almacenan camisetas de 5 equipos que son las que más se venden:
Barcelona, Inter Miami, PSG, Manchester City y Real Madrid.
Los puntos 2 y 3 deben utilizar la misma función (calcular_totales). La misma debe poder
sumar por filas o por columnas. Además, deberán utilizar la función estimar_stock que recibe
una lista de totales, una lista de strings con el nombre de cada total y reciba por parámetro
cuál es el límite que debe tomar para informar.
Realizar un menú de opciones:

1. Obtener existencias: para ello deberá generar una función que cargue
secuencialmente, de tal forma que la intersección de cada fila y cada columna
corresponda a la cantidad de camisetas de un equipo en un depósito. Esto es carga
secuencial.
2. Mostrar depósitos que tienen en stock más de 10.000 camisetas.
3. Mostrar equipos que hay en stock más de 5.000 camisetas.
4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se
encuentra.
5. Cargar ventas: se deberá poder cargar ventas de un determinado producto para un
determinado depósito. Esto es carga distribuida o aleatoria. Al cargarse las ventas
se deben restar los productos vendidos del stock y generar una matriz con la
recaudación que reciba el listado de precios por parámetro, en caso de no recibir un
listado deberá tener un precio de 100 cada producto. Utilizar parámetro opcional.
"""

from funcion import *

equipos = ["Barcelona", "Inter Miami", "PSG", "Manchester City", "Real Madrid"]
deposito = ["Tierra del Fuego", "Tucumán", "Mendoza", "Bs As", "Misiones", "Santa Fé"]

def cargar_ventas(deposito, equipos, existencias, recaudacion, precios=None):
    print("Seleccione el depósito:")
    i = 0
    while i < len(deposito):
        print(f"{i + 1}. {deposito[i]}")
        i += 1
    deposito = int(input("Ingrese el número del depósito: ")) - 1

    print("Seleccione el equipo:")
    j = 0
    while j < len(equipos):
        print(f"{j + 1}. {equipos[j]}")
        j += 1
    equipos = int(input("Ingrese el número del equipo: ")) - 1

    cantidad_ventas = int(input("Ingrese la cantidad de camisetas vendidas: "))
    # Verificar que haya suficiente stock para la venta
    if existencias[deposito][equipos] >= cantidad_ventas:
        existencias[deposito][equipos] -= cantidad_ventas

        # Determinar el precio, ya sea de la lista de precios o el valor por defecto de 100
        precio = precios[equipos] if precios else 100
        recaudacion[deposito][equipos] += cantidad_ventas * precio
        print(f"Venta realizada: {cantidad_ventas} camisetas de {equipos[equipos]} en {deposito[deposito]}")
    else:
        print("Stock insuficiente para realizar la venta.")

ejecutar = True
carga = True

existencias = cargar_existencias(len(deposito), len(equipos))
recaudacion =  [[0 for _ in range(len(equipos))] for _ in range(len(deposito))]

while ejecutar == True:

    print("Seleccione opcion que desea realizar: ")
    print("1. Obtener existencias ") 
    print("2. Calcular total de camisetas por depósito ")
    print("3. Calcular total de camisetas por equipo ")
    print("4. Estimar stock ")
    print("5. Mostrar depositos con mas de 10.000 camisetas")
    print("6. Mostrar equipos con más de 5,000 camisetas")
    print("7. Obtener máxima cantidad de camisetas de cada equipo y su depósito")
    print("8. Cargar ventas ")
    print("9. Salir ")

    opcion = input("Seleccione una opcion: ")


    if opcion == "1":
        print("Existencias de caminesaas por deposito y equipo: ")
        i = 0
        while i < len(deposito):
            print(f"{deposito[i]}: {existencias[i]}")

    elif opcion == "2":
        totales_deposito = calcular_totales(existencias, por_la_fila=True)
        print("Total de camisetas por deposito: ")
        i = 0
        while i < len(totales_deposito):
            print(f"{deposito[i]}: {totales_deposito[i]}")
            i += 1

    elif opcion == "3":
        totales_equipos = calcular_totales(existencias, por_la_fila=False)
        print("Total de camisetas por equipo: ")
        i = 0
        while i < len(totales_equipos):
            print(f"{equipos[i]}: {totales_equipos[i]}")
            i += 1

    elif opcion == "4":
        limite = int(input("Ingrese el limite de stock para estimacion: "))
        totales = calcular_totales(existencias, por_la_fila=True)
        excedidos = estimar_stock(totales, deposito, limite)
        if excedidos:
            print("Depositos con stock superior al limite: ")
            i = 0
            while i < len (excedidos):
                print(excedidos[i])
                i += 1
        else: 
            print("Ninguno de los depositos supera el limite. ")

    elif opcion == "5":
        # Mostrar depósitos que tienen en stock más de 10.000 camisetas.
        totales_deposito = calcular_totales(existencias, por_la_fila=True)
        excedidos = estimar_stock(totales_deposito, deposito, 10000)
        if excedidos:
            print("Depositos con mas de 10.000 camisetas: ")
            i = 0
            while i < len(excedidos):
                print(excedidos[i])
                i += 1
        else:
            print("Ningun deposito obtuvo mas de 10.000 camisetas.")

    elif opcion == "6":
        # Mostrar equipos que hay en stock más de 5.000 camisetas.
        totales_equipos = calcular_totales(existencias, por_la_fila=False)
        excedidos = estimar_stock(totales_equipos, equipos, 5000)
        if excedidos:
            print("Equipos con mas de 5.000 camisetas: ")
            i = 0 
            while i < len(excedidos):
                print(excedidos[i])
                i += 1
        else:
            print( "Ningun equipo tiene mas de 5,000 camisetas.")

    elif opcion == "7":
        # 4. Obtener máxima cantidad de camisetas de cada equipo. Mostrar en qué depósito se encuentra.
        maximos_por_equipo = obtener_maximo_por_equipo(existencias, equipos, deposito)
        print("Maxima cantidad de camisetas de cada equipo y su deposito: ")
        for equipo, maxima_cantidad, deposito in maximos_por_equipo:
            print(f"{equipo}: {maxima_cantidad} en {deposito}")

    elif opcion == "8":
        precios = [110, 120, 140, 130, 150]  
        cargar_ventas(deposito, equipos, existencias, recaudacion, precios)

    elif opcion == "9":
        print("Se salió del ejercicio")
        break
        
    else:
            print("Opción no válida. Intente de nuevo.")
