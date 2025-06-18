# Programación tradicional
# Ejemplo: Temperatura

# Definición de variables globales
dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [0] * 7  # Lista para 7 días de la semana

# Función para ingresar temperaturas diarias
def ingresar_temperaturas():
    global temperaturas
    for i in range(7):
        temp = float(input(f"Ingrese la temperatura del {dias[i]}: "))
        temperaturas[i] = temp

# Función para calcular el promedio semanal
def calcular_promedio():
    global temperaturas
    suma = sum(temperaturas)
    promedio = suma / 7
    return promedio

# Imprimir las temperaturas diarias y promedio semanal de temperaturas
def main():
    print("Registro de temperaturas semanales")
    ingresar_temperaturas()
    promedio = calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f}°C")

# Ejecutar el uso de las funciones en la programación tradicional
main()
