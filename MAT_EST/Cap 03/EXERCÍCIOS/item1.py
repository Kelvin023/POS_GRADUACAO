import math

def calcular_area_circulo():
    raio = float(input("Digite o raio do círculo: "))
    area = math.pi * raio**2
    print(f"A área do círculo com raio {raio} é: {area:.2f}")

calcular_area_circulo()