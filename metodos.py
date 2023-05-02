cadena = "Te voy a escribir la cancion mas bonita del mundo"

# Utilizando el método count para contar la cantidad de veces que aparece una subcadena
subcadena = "la"
cantidad = cadena.count(subcadena)
print(f"La subcadena '{subcadena}' aparece {cantidad} veces en la cadena.")

# Utilizando el método find para buscar la posición de una subcadena
subcadena = "cancion"
posicion = cadena.find(subcadena)
print(f"La subcadena '{subcadena}' comienza en la posición {posicion}.")

# Utilizando el método len para obtener la longitud de una cadena
longitud = len(cadena)
print(f"La cadena tiene {longitud} caracteres.")

# Utilizando el método split para dividir una cadena en varias subcadenas
subcadenas = cadena.split()
print("Las subcadenas son:")
for subcadena in subcadenas:
    print(subcadena)

# Utilizando el método join para unir varias subcadenas en una cadena
subcadenas = ["Te", "voy", "a", "escribir", "la", "cancion", "mas", "bonita", "del", "mundo"]
cadena_unida = " ".join(subcadenas)
print(f"La cadena unida es: '{cadena_unida}'")

# Utilizando el método strip para eliminar espacios en blanco al principio y al final de una cadena
cadena = "    Te voy a escribir la cancion mas bonita del mundo   "
cadena_sin_espacios = cadena.strip()
print(f"La cadena sin espacios es: '{cadena_sin_espacios}'")

# Utilizando el método replace para reemplazar una subcadena por otra
cadena_nueva = cadena.replace("bonita", "hermosa")
print(f"La cadena reemplazada es: '{cadena_nueva}'")

# Utilizando el método upper y lower para convertir una cadena a mayúsculas o minúsculas
cadena_mayusculas = cadena.upper()
print(f"La cadena en mayúsculas es: '{cadena_mayusculas}'")

cadena_minusculas = cadena.lower()
print(f"La cadena en minúsculas es: '{cadena_minusculas}'")
