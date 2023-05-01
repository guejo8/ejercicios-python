# Función para dibujar el tablero
def dibujar_tablero(tablero):
    print("  1 2 3")
    for i in range(3):
        print(str(i+1) + " " + " ".join(tablero[i]))

# Función para pedir la fila y la columna al usuario
def pedir_coordenadas():
    while True:
        coordenadas = input("Elige una posición (fila, columna): ")
        if len(coordenadas) != 2:
            print("Coordenadas inválidas. Inténtalo de nuevo.")
            continue
        fila, columna = coordenadas
        if fila not in ["1", "2", "3"] or columna not in ["1", "2", "3"]:
            print("Coordenadas inválidas. Inténtalo de nuevo.")
            continue
        return int(fila) - 1, int(columna) - 1

# Función para actualizar el tablero con el movimiento del jugador
def actualizar_tablero(tablero, fila, columna, jugador):
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = jugador
        return True
    else:
        return False

# Función para determinar si hay un ganador
def hay_ganador(tablero, jugador):
    # Comprobar filas
    for fila in tablero:
        if fila == [jugador] * 3:
            return True
    # Comprobar columnas
    for j in range(3):
        if [tablero[i][j] for i in range(3)] == [jugador] * 3:
            return True
    # Comprobar diagonales
    if [tablero[i][i] for i in range(3)] == [jugador] * 3:
        return True
    if [tablero[i][2-i] for i in range(3)] == [jugador] * 3:
        return True
    return False

# Función principal del juego
def jugar_tres_en_raya():
    tablero = [[" " for j in range(3)] for i in range(3)]
    jugador_actual = "X"
    dibujar_tablero(tablero)
    while True:
        print("Turno del jugador", jugador_actual)
        fila, columna = pedir_coordenadas()
        if actualizar_tablero(tablero, fila, columna, jugador_actual):
            dibujar_tablero(tablero)
            if hay_ganador(tablero, jugador_actual):
                print("¡Ganó el jugador", jugador_actual, "!")
                break
            elif all(celda != " " for fila in tablero for celda in fila):
                print("¡Empate!")
                break
            jugador_actual = "O" if jugador_actual == "X" else "X"
        else:
            print("Posición ocupada. Inténtalo de nuevo.")

# Ejecutar el juego
jugar_tres_en_raya()
