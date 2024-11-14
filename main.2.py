"""
Ejercicio 2:
En este ejercicio deberán programar funciones para realizar operaciones sobre matrices
cuadradas. Por ello se debe validar que las matrices que se reciben tengan la misma cantidad
de filas y columnas.
1. Generar una función que calcule la media geométrica de filas o columnas de una matriz
cuadrada.
2. Generar una función que calcule la suma de las diagonales principal y secundaria de una
matriz.
Ejemplo:
1 2 3
4 5 6
7 8 9
Devuelve 30.
3. Generar una función que reciba una matriz y devuelva su transpuesta.
4. A la función del ejercicio 2 agregar un parámetro que permita seleccionar si lo que se
pretende recibir como retorno es la suma de ambas diagonales, solo la de la diagonal
principal o solo la de la diagonal secundaria.
"""
from funcion2 import *

# 1. Media geométrica
print('Media geométrica de filas:', media_geometrica("matriz", 'fila'))
print('Media geométrica de columnas:', media_geometrica("matriz", 'columna'))
    
# 2. Suma de diagonales
print('Suma de ambas diagonales:', suma_diagonales("matriz"))
    
# 3. Transpuesta de la matriz
print('Matriz transpuesta:')
transpuesta_matriz = transpuesta("matriz")
for fila in transpuesta_matriz:
    print(fila)
    
#4. Suma de diagonales con opción
print('Suma de la diagonal principal:', suma_diagonales_opcional("matriz", 'principal'))
print('Suma de la diagonal secundaria:', suma_diagonales_opcional("matriz", 'secundaria'))
print('Suma de ambas diagonales:', suma_diagonales_opcional("matriz", 'ambas'))