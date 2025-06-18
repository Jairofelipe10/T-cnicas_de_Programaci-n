# Programación Orientado a Objetos (POO)
# Ejemplo: Información diaria del clima

# Clase principal para manejar el clima semanal
class ClimaSemanal:
    def __init__(self):
        self._dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self._temperaturas = [0] * 7  # Encapsulamiento

    # Ingresar temperaturas (encapsulado)
    def ingresar_temperaturas(self):
        for i in range(7):
                    temp = float(input(f"Ingrese la temperatura del {self._dias[i]}: "))
                    self._temperaturas[i] = temp

    # Calcular el promedio (encapsulado)
    def calcular_promedio(self):
        suma = sum(self._temperaturas)
        return suma / 7

    # Obtener temperaturas (atrayecte)
    def get_temperaturas(self):
        return self._temperaturas

# Mostrar las temperaturas y el promedio  (herencia)
class ClimaDetallado(ClimaSemanal):
    def mostrar_detalles(self):
        temps = self.get_temperaturas()
        print("\nTemperaturas de la semana:")
        for i in range(7):
            print(f"{self._dias[i]}: {temps[i]:.2f}°C")
        print(f"Promedio semanal: {self.calcular_promedio():.2f}°C")

# Uso de los métodos en la POO
def main():
    print("Registro de temperaturas semanales")
    clima = ClimaDetallado()  # Instancia de temperaturas y el promedio
    clima.ingresar_temperaturas()
    clima.mostrar_detalles()

# Ejecutar el uso de las funciones en la POO
if __name__ == "__main__":
    main()