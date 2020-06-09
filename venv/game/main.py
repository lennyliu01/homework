import game as g

def main():
    all_games = ["SubtractSquare"]
    game = input("Please select one game from following: " + str(all_games))
    while game not in all_games:
        print("the entered game name is invalid")
        game = input("Please reselect one game from following: " + str(all_games))
    if game == all_games[0]:
        is_Player1_First = input("Is player 1 goes first? Enter T/F")
        while is_Player1_First not in ["T", "F"]:
            is_Player1_First = input("what you enter is invalid? Enter T/F")
        if is_Player1_First == "T":
            is_Player1_First = True
        else:
            is_Player1_First = False

        state = int(input("Please enter a positive number: "))

        subtractSquare = g.SubtractSquare(is_Player1_First, state)
        player = subtractSquare.get_current_player()
        if player == "Player 1":
            check_player = "Player 2"
        else:
            check_player = "Player 1"

        while not subtractSquare.is_winner(check_player):
            print("The current player is: ", player)
            print("The current state value is: ", subtractSquare.get_state())
            print("The possible moves are: ", subtractSquare.get_possible_moves())

            move = int(input("make your move: "))
            subtractSquare.make_move(move)
            print("The new state value is: ", subtractSquare.get_state())
            check_player = player
            player = subtractSquare.get_current_player()

        print("Congratulation! The winner is ", check_player)


if __name__ == '__main__':
    main()
