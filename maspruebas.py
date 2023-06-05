# Empaquetar y desempaquetar argumentos con tuplas
def suma(a, b, c):
    return a + b + c

valores_tupla = (1, 2, 3)
resultado_tupla = suma(*valores_tupla)
print(resultado_tupla)  # Salida: 6

# Empaquetar y desempaquetar argumentos con listas
def multiplicacion(x, y, z):
    return x * y * z

valores_lista = [4, 5, 6]
resultado_lista = multiplicacion(*valores_lista)
print(resultado_lista)  # Salida: 120

# Empaquetar y desempaquetar argumentos con objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

def saludar(persona):
    print(f"Hola, soy {persona.nombre} y tengo {persona.edad} años.")

persona1 = Persona("Juan", 30)
saludar(persona1)  # Salida: Hola, soy Juan y tengo 30 años.
