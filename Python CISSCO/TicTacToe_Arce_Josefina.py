escribe un simple programa que simule jugar a tic-tac-toe (nombre en inglés) con el usuario. Para hacerlo más fácil, hemos decidido simplificar el juego. Aquí están las reglas:

la maquina (por ejemplo, el programa) jugará utilizando las 'X's;
el usuario (por ejemplo, tu) jugarás utilizando las 'O's;
el primer movimiento es de la maquina - siempre coloca una 'X' en el centro del tablero;
todos los cuadros están numerados comenzando con el 1 (observa el ejemplo para que tengas una referencia)
el usuario ingresa su movimiento introduciendo el número de cuadro elegido - el número debe de ser valido, por ejemplo un valor entero mayor que 0 y menor que 10, y no puede ser un cuadro que ya esté ocupado;
el programa verifica si el juego ha terminado - existen cuatro posibles veredictos: el juego continua, el juego termina en empate, tu ganas, o la maquina gana;
la maquina responde con su movimiento y se verifica el estado del juego;
no se debe implementar algún tipo de inteligencia artificial - la maquina elegirá un cuadro de manera aleatoria, eso es suficiente para este juego.


-------------------
import random

# Dibuja el tablero
def draw_board(board):
    print(" {} | {} | {} ".format(board[1], board[2], board[3]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[4], board[5], board[6]))
    print("---|---|---")
    print(" {} | {} | {} ".format(board[7], board[8], board[9]))

# Verifica si alguien ha ganado
def check_win(board, player):
    # Revisa las filas
    for i in range(1, 8, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    # Revisa las columnas
    for i in range(1, 4):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    # Revisa las diagonales
    if board[1] == board[5] == board[9] == player:
        return True
    if board[3] == board[5] == board[7] == player:
        return True
    # Si no hay ganador
    return False

# Juega
def play_game():
    board = {i: " " for i in range(1, 10)}  # Crea el tablero
    board[5] = "X"  # La maquina comienza jugando en el centro
    player = "O"  # El jugador comienza jugando en cualquier otro lugar
    print("¡Comenzamos!")
    draw_board(board)
    # Ciclo principal del juego
    while True:
        # Turno del jugador
        move = int(input("Tu turno. Elige un cuadro (1-9): "))
        if board[move] != " ":
            print("¡Cuadro ocupado! Elige otro.")
            continue
        board[move] = player
        draw_board(board)
        # Revisa si el jugador ganó
        if check_win(board, player):
            print("¡Ganaste!")
            return
        # Revisa si hay empate
        if all(value != " " for value in board.values()):
            print("¡Empate!")
            return
        # Turno de la maquina
        print("Turno de la maquina...")
        while True:
            move = random.randint(1, 9)
            if board[move] == " ":
                board[move] = "X"
                break
        draw_board(board)
        # Revisa si la maquina ganó
        if check_win(board, "X"):
            print("¡Perdiste!")
            return

# Inicia el juego
play_game()


Este programa utiliza un diccionario para representar el tablero del juego. La función draw_board imprime el tablero en la consola, la función check_win verifica si alguien ha ganado y la función play_game es el ciclo principal del juego que se encarga de solicitar los movimientos del usuario y de la maquina, y de revisar el estado del juego en cada turno.
----------------------

<iframe width="560" height="315" src="https://www.youtube.com/embed/w0LqU99RRy8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
----------
