#importo libreria math
import math

#variables de entrada
precio = float(input("Ingrese el precio de suscripción en números: "))
usuariosNormales = float(input("Ingrese la cantidad de usuarios normales en números:"))
usuariosPremium = float(input("Ingrese la cantidad de usuarios premium en números:"))
gastoTotal = float(input("Ingrese el gasto total en números:"))

#calculo utilidades
utilidades = (precio * usuariosNormales + precio * 1.5 * usuariosPremium) - gastoTotal

#imprimo el resultado
print(f"las utilidades de este año son: {(utilidades):.2f}")