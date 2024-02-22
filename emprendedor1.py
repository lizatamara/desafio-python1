#importo libreria math
import math

#variables de entrada
precio = float(input("Ingrese el precio de suscripción en números: "))
usuarios = float(input("Ingrese la cantidad de usuarios en números: "))
gastoTotal = float(input("Ingrese el gasto total en números: "))

#calculo utilidades
utilidades = precio * usuarios - gastoTotal

#imprimo el resultado
print(f"las utilidades de este año son: {utilidades:.2f}")