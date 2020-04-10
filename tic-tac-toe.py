def tic_tac_toe():

    board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    game_ended = False

    #board = clean_board
    graphic_board = f'''
    | {board[7]} | {board[8]} | {board[9]} |
    -------------
    | {board[4]} | {board[5]} | {board[6]} |
    -------------
    | {board[1]} | {board[2]} | {board[3]} |'''

    print(graphic_board)

    # Introduction to the game

    print("The positions on the board correspond to the position of the numbers 1-9 in the numerical pad of your keyboard")

    # Ask player 1 which symbol s(he) wants to use. Assin¡gn player 2 the other symbol

    player_one_sym = input("Player 1, do you want to play with X or with O?: ").upper()
    if player_one_sym == "X":
        player_two_sym = "O"
    else:
        player_two_sym = "X"
    print(f'Player 2, you play with {player_two_sym}')

    # Game starts

    while game_ended == False:

        #Player one plays:

        board[int(input("Player one, select the cell where you want to introduce your symbol: "))] = player_one_sym
        graphic_board = f'''
    | {board[7]} | {board[8]} | {board[9]} |
    -------------
    | {board[4]} | {board[5]} | {board[6]} |
    -------------
    | {board[1]} | {board[2]} | {board[3]} |'''
        print(graphic_board)

        # Chequear si el movimiento de P1 ha hecho 3 en raya!!!
        if (
    (board[1] == player_one_sym and board[2] == player_one_sym and board[3] == player_one_sym) or
    (board[4] == player_one_sym and board[5] == player_one_sym and board[6] == player_one_sym) or
    (board[7] == player_one_sym and board[8] == player_one_sym and board[9] == player_one_sym) or
    (board[1] == player_one_sym and board[4] == player_one_sym and board[7] == player_one_sym) or
    (board[2] == player_one_sym and board[5] == player_one_sym and board[8] == player_one_sym) or
    (board[3] == player_one_sym and board[6] == player_one_sym and board[9] == player_one_sym) or
    (board[7] == player_one_sym and board[5] == player_one_sym and board[3] == player_one_sym) or
    (board[1] == player_one_sym and board[5] == player_one_sym and board[9] == player_one_sym)
        ):

            print("\nPlayer 1 won!")
            game_ended = True
            break

        #Player two plays:

        board[int(input("Player two, select the cell where you want to introduce your symbol: "))] = player_two_sym
        graphic_board = f'''
    | {board[7]} | {board[8]} | {board[9]} |
    -------------
    | {board[4]} | {board[5]} | {board[6]} |
    -------------
    | {board[1]} | {board[2]} | {board[3]} |'''
        print(graphic_board)

        # # Chequear si el movimiento de P2 ha hecho 3 en raya!!! (un if, si se cumple poner game_ended = True)

        if (
        (board[1] == player_two_sym and board[2] == player_two_sym and board[3] == player_two_sym) or
        (board[4] == player_two_sym and board[5] == player_two_sym and board[6] == player_two_sym) or
        (board[7] == player_two_sym and board[8] == player_two_sym and board[9] == player_two_sym) or
        (board[1] == player_two_sym and board[4] == player_two_sym and board[7] == player_two_sym) or
        (board[2] == player_two_sym and board[5] == player_two_sym and board[8] == player_two_sym) or
        (board[3] == player_two_sym and board[6] == player_two_sym and board[9] == player_two_sym) or
        (board[7] == player_two_sym and board[5] == player_two_sym and board[3] == player_two_sym) or
        (board[1] == player_two_sym and board[5] == player_two_sym and board[9] == player_two_sym)
        ):

            print("\nPlayer 2 won!")
            game_ended = True

      # Cuando el juego acaba, preguntar si se quiere volver a jugar
      # En caso positivo (Y), volver a lanzar el juego. En caso negativo (N),
      # escribir un mensaje de despedida y acabar programa

        def replay():

            play_again = input("Do you want to play again?: (Y/N)")

            if play_again == "Y":
                tic_tac_toe()
            else:
                print("You have left the game")
    if game_ended == True:
        replay()

tic_tac_toe()
