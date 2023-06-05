#Argumentos posicionales en Python:

def area_triangulo(base, altura):
    return (base * altura) / 2

resultado = area_triangulo(4, 6)
print(resultado)  # Output: 12.0

#Argumentos nominales en Python:

def crear_agenda(nombre, edad, ciudad):
    return {"nombre": nombre, "edad": edad, "ciudad": ciudad}

datos = crear_agenda(nombre="Ana", edad=25, ciudad="Madrid")
print(datos)  # Output: {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid'}

#Ejemplo de argumentos inmutables

def modificar_numero(numero):
    numero += 1
    print(numero)  # 11 (valor modificado dentro de la función)
x = 10
modificar_numero(x)
print(x)  #  10 (valor original sin cambios)

#Ejemplo de argumentos mutables

def modificar_lista(lista):
    lista.append(4)
    print(lista)  # [1, 2, 3, 4] Lista modificada dentro de la función

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print(mi_lista)  # [1, 2, 3, 4] Lista original modificada

# Ejemplo 1: Función con argumento por defecto

def saludar(nombre, mensaje="¡Hola!"):
    print(f"{mensaje} {nombre}")

saludar("Imanol")  # Salida: ¡Hola! Imanol
saludar("Ruth", "¡Buenos días!")  # Salida: ¡Buenos días! Ruth

# Ejemplo 2: Función con parámetro por defecto

def calcular_potencia(base, exponente=2):
    return base ** exponente

resultado2 = calcular_potencia(2, 3)  # Calcula 2^3
print(resultado2)  # Salida: 8

#Argumentos arbitrarios posicionales

def sumar(*numeros):
    total = 0
    for num in numeros:
        total += num
    return total

resultado = sumar(1, 2, 3, 4, 5)
print(resultado)  # Salida: 15

#Argumentos arbitrarios de palabras clave

def mostrar_info(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")
# Salida:
# nombre: Juan
# edad: 30
# ciudad: Madrid

def bienvenida(nombre):
   print('¡Bienvenido a Python', nombre + '!')
   return

bienvenida('Alf')
#Salida: ¡Bienvenido a Python Alf!

#Hacer inmutable argumento mutable

def modificar_lista(lista):
    copia_lista = lista[:]
    copia_lista.append(4)
    copia_lista[0] = "Nuevo valor"
    print("Dentro de la función:")
    print("Copia de lista:", copia_lista) #Salida  ['Nuevo valor', 2, 3, 4]

lista_original = [1, 2, 3]

print("Antes de llamar a la función:")
print("Lista original:", lista_original) #Salida [1, 2, 3]

modificar_lista(lista_original)

print("Después de llamar a la función:")
print("Lista original:", lista_original) #Salida [1, 2, 3]


def modificar_lista(lista):
    copia_lista = lista.copy()  # Creamos una copia independiente de la lista original
    copia_lista.append("nuevo")  # Agregamos la palabra "nuevo" a la copia de la lista
    copia_lista[0] = "cambio"  # Modificamos el primer elemento de la copia de la lista
    print("Dentro de la función:")
    print("Copia de lista:", copia_lista) #Salida ['cambio', 'amigo', 'nuevo']

lista_original = ["hola", "amigo"]

print("Antes de llamar a la función:")
print("Lista original:", lista_original) # Salida ['hola', 'amigo']

modificar_lista(lista_original)

print("Después de llamar a la función:")
print("Lista original:", lista_original) # Salida ['hola', 'amigo']

#Empaquetar y desempaquetar