#importo libreria math
import math

#variables de entrada
radio = float(input("Ingrese el radio en Kilómetros: "))
gravedad = float(input("Ingrese la constante g:"))

#paso el radio de kilómetros a metros
radio = radio * 1000

#calculo la velocidad de escape
velocidad = math.sqrt(2 * radio * gravedad)

#imprimo el resultado
print(f'La velocidad de escape es {velocidad:.1f} m/s')