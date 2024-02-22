#importo libreria math
import math

#variables de entrada
precio = float(input("Ingrese el precio de suscripción en números: "))
usuarios = float(input("Ingrese la cantidad de usuarios en números: "))
gastoTotal = float(input("Ingrese el gasto total en números: "))
utilidadesAnterior = float(input("Ingrese las utilidades del año anterior en números: "))

#calculo utilidades
utilidades = precio * usuarios - gastoTotal

#calculo razon entre este año y el anterior

razonUtilidades = utilidades / utilidadesAnterior

#imprimo el resultado
print(f"la razón entre las utilidades de este año y el anterior es: {(razonUtilidades):.2f}")