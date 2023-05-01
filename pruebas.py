#TIPO DE INSTRUCCIONES E INDENTACCION

#Instrucciones simples Ejemplo:
b = 12
c = (2 + 2 + 8)
a = 'Hola'
print (a)
#Instrucciones compuestas Ejemplo:
if b == c:
    print (a)

#---------------------------------------------------------
#correcta


x = 5
if x > 0:
    print("x es positivo")
else:
    print("x es negativo")


#incorrecta

x = 5
if x > 0:
    print("x es positivo")
        print("x es mayor que cero")
else:
    print("x es negativo")


#COMENTARIOS

# Se pueden comentar de este modo varias filas seguidas
# Se pide al usuario que ingrese el primer y segundo número
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: ")) # Se puede comentar al final de la fila

"""Se suman los dos números ingresados y se almacena
el resultado en la variable 'suma'. Para comentar varias filas es conveniente utilizar las triples comillas. """

suma = num1 + num2
# Se muestra el resultado en la pantalla
print("La suma de", num1, "y", num2, "es", suma)




#USANDO BUCLES E ITERACIONES

def nombres():
    '''Pide al usuario que ingrese el primer nombre de un estudiante en clase
    hasta que se ingrese una string vacía. Luego la función imprime el número 
    de estudiantes con cada nombre que se ingresó.
    '''

    nombre = ''
    nombres = []
    nombre = input('Enter next nombre: ')

    while nombre != '':  # Mientras que nombre no sea una string vacia
        nombres.append(nombre)
        nombre = input('Enter next nombre: ')

    # Creamos un diccionario con la estructura nombre:ocurrencias
    ocurrencias_nombre = {n:nombres.count(n) for n in nombres}

    # Iteramos a traves de las claves del diccionario
    for k in ocurrencias_nombre.keys(): 
        singular = True if ocurrencias_nombre[k] < 2 else False

        if singular:
            print('Hay {} estudiante llamado {}'.format(ocurrencias_nombre[k], k))
        else:
            print('Hay {} estudiantes llamados {}'.format(ocurrencias_nombre[k], k))

nombres()