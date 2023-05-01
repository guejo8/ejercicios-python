# Función para sumar dos números
def sumar(num1, num2):
    return num1 + num2

# Función para restar dos números
def restar(num1, num2):
    return num1 - num2

# Función para multiplicar dos números
def multiplicar(num1, num2):
    return num1 * num2

# Función para dividir dos números
def dividir(num1, num2):
    return num1 / num2

# Función principal de la calculadora
def calcular():
    while True:
       # Pedir los números al usuario
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        # Pedir la operación al usuario
        operacion = input("¿Qué operación quieres hacer? (+, -, *, /) ")
        if operacion not in ["+", "-", "*", "/"]:
            print("Operación inválida. Inténtalo de nuevo.")
            continue

        # Realizar la operación correspondiente
        if operacion == "+":
            resultado = sumar(num1, num2)
        elif operacion == "-":
            resultado = restar(num1, num2)
        elif operacion == "*":
            resultado = multiplicar(num1, num2)
        else:
            resultado = dividir(num1, num2)

        # Imprimir el resultado
        print("El resultado es:", resultado)
        
        # Preguntar al usuario si quiere hacer otra operación
        continuar = input("¿Quieres hacer otra operación? (S/N) ")
        if continuar.upper() != "S":
            break

# Ejecutar la calculadora
calcular()
