from stockfish import Stockfish
import re

# Download link: https://stockfishchess.org/download/


def play_on_console():
    stockfish = Stockfish(r"stockfish/stockfish_13_win_x64_bmi2.exe")
    usr_move = ""
    print(stockfish.get_board_visual())

    while(1):
        usr_move = str(input("Enter move: "))

        if usr_move == 'q' or usr_move == 'quit':
            break

        if usr_move == 'h' or usr_move == 'help':
            print("\nHelp:")
            print("\nRows are annotated 8 to 1 from top to bottom")
            print("Columns are annotated a to h from left to right")
            print("\nIf you wish to move a piece from column b row 2 to column b row 3,")
            print("Enter your move as b2b3\n")
            continue

        if re.match('([a-h][1-8]){2}', usr_move) == None:
            print("Move did not match the pattern '([a-h][1-8]){2}'\n")
            continue

        if stockfish.is_move_correct(usr_move) == False:
            print("Invalid move\n")
            continue

        stockfish.make_moves_from_current_position([usr_move])
        print(stockfish.get_board_visual())

        # Computer's turn
        print(f"Bot move: {stockfish.get_best_move()}")

        stockfish.make_moves_from_current_position([stockfish.get_best_move()])
        print(stockfish.get_board_visual())


if __name__ == "__main__":
    play_on_console()
