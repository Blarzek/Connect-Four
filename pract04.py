import games

dificultad = raw_input("Elige el nivel de dificultad Facil -> F o Dificil -> D?: ")
while dificultad.lower() != 'f' and dificultad.lower() != 'd':
    dificultad = raw_input("Introduzca un nivel de dificultad valido. Facil -> F o Dificil -> D: ")

print "Introduzca las dimensiones del tablero."
horizontal = raw_input("Horizontal: ")
while True:
    try:
        int(horizontal)
    except ValueError:
        print "-------------------"
        horizontal = raw_input("Introduzca un numero valido: ")
    else:
        break

vertical = raw_input("Vertical: ")
while True:
    try:
        int(vertical)
    except ValueError:
        print "-------------------"
        vertical = raw_input("Introduzca un numero valido: ")
    else:
        break

k_en_raya = raw_input("Introduzca el numero de fichas en raya que desea jugar (3 en raya, 4 en raya, etc.): ")
while True:
    try:
        int(k_en_raya)
    except ValueError:
        print "-------------------"
        k_en_raya = raw_input("Introduzca un numero valido: ")
    else:
        if k_en_raya < 3:
            k_en_raya = raw_input("Introduzca un numero que mayor que 2:")
        if k_en_raya > horizontal or k_en_raya > vertical:
            print "-------------------"
            print("Imposible jugar asi con este tablero ({0}x{1}).".format(vertical, horizontal))
            k_en_raya = raw_input("Introduzca un numero que se adapte a ese tablero:")
        else:
            break

vertical = int(vertical)
horizontal = int(horizontal)
k_en_raya = int(k_en_raya)

game = games.ConnectFour(vertical, horizontal, k_en_raya)
state = game.initial
player="H"

while True:
    print "Jugador a mover:", game.to_move(state)
    game.display(state)
    # Imprimimos la ristra de numeros que equivale a las columnas del tablero
    print ' '.join(str(x) for x in xrange(1, horizontal + 1))
    print "-------------------"

    if player.lower() == 'h':
        coor = raw_input("Introduzca un numero de columna valido o H para ayuda: ")
        if coor.lower() == 'h':
            print "Thinking...."
            move = games.alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=game.dificil)
            x, y = move
            print "Aconsejamos: ", y
            coor = raw_input("Ahora introduzca un numero de columna: ")
        while True:
            try:
                int(coor)
            except ValueError:
                coor = raw_input("Introduzca un numero de columna valido: ")
            else:
                coor = int(coor)
                if coor > horizontal or coor < 1:
                    coor = raw_input("Elige un numero de columna que sea del tablero (1-{0}): ".format(horizontal))
                else:
                    break

        if game.check(state, coor) != 0:
            state = game.make_move((game.check(state, coor), coor), state)
            player = 'M'
        else:
            print "Introduzca un movimiento valido."
            player = 'H'
    else:
        print "Thinking..."
        # Dependiendo de la dificultad escogida, se invoca una heuristica u otra
        if dificultad.lower() == 'f':
            move = games.alphabeta_search(state, game, 3, None, game.facil)
            state = game.make_move(move, state)
        else:
            move = games.alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=game.dificil)
            state = game.make_move(move, state)
        x, y = move
        print "Ultimo movimiento: columna ", y
        player = 'H'
    print "-------------------"
    if game.terminal_test(state):
        game.display(state)
        print "Final de la partida"
        break