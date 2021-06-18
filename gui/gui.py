# Graphical User Interface (GUI) for playing chess
# Written by Rutuparn Pawar [InputBlackBoxOutput]

import tkinter
from tkinter import *
import tkinter.messagebox as msgbox

import platform
from stockfish import Stockfish
import chess

# -------------------------------------------------------------------------------------------
# Unicode for chess pieces
# white king	  ♔   U+2654
# white queen	  ♕   U+2655
# white rook	  ♖   U+2656
# white bishop    ♗   U+2657
# white knight    ♘   U+2658
# white pawn	  ♙   U+2659
# black king	  ♚   U+265A
# black queen	  ♛   U+265B
# black rook	  ♜   U+265C
# black bishop    ♝   U+265D
# black knight    ♞   U+265E
# black pawn	  ♟   U+265F

unicode_map = {"K": "\u2654",
               "Q": "\u2655",
               "R": "\u2656",
               "B": "\u2657",
               "N": "\u2658",
               "P": "\u2659",

               "k": "\u265A",
               "q": "\u265B",
               "r": "\u265C",
               "b": "\u265D",
               "n": "\u265E",
               "p": "\u265F",

               "-": " "
               }
# ----------------------------------------------------------------------------------
# Button map
btn_map = {
    "a8": 0, "b8": 1, "c8": 2, "d8": 3, "e8": 4, "f8": 5, "g8": 6, "h8": 7,
    "a7": 8, "b7": 9, "c7": 10, "d7": 11, "e7": 12, "f7": 13, "g7": 14, "h7": 15,
    "a6": 16, "b6": 17, "c6": 18, "d6": 19, "e6": 20, "f6": 21, "g6": 22, "h6": 23,
    "a5": 24, "b5": 25, "c5": 26, "d5": 27, "e5": 28, "f5": 29, "g5": 30, "h5": 31,
    "a4": 32, "b4": 33, "c4": 34, "d4": 35, "e4": 36, "f4": 37, "g4": 38, "h4": 39,
    "a3": 40, "b3": 41, "c3": 42, "d3": 43, "e3": 44, "f3": 45, "g3": 46, "h3": 47,
    "a2": 48, "b2": 49, "c2": 50, "d2": 51, "e2": 52, "f2": 53, "g2": 54, "h2": 55,
    "a1": 56, "b1": 57, "c1": 58, "d1": 59, "e1": 60, "f1": 61, "g1": 62, "h1": 63
}
# ----------------------------------------------------------------------------------


class GUI(Tk):
    def __init__(self, width, height):
        super().__init__()

        self.title("Chess")
        self.geometry(f"{width}x{height}")
        self.wm_resizable(width=False, height=False)

        self.usr_move = ""
        self.game_over = False

        self.bot = Stockfish(r"stockfish/stockfish_13_win_x64_bmi2.exe")

    # -------------------------------------------------------------------------------
    # Menu bar

    def new_game(self):
        self.bot.set_fen_position(
            "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        self.update_board()
        self.remove_marking()
        self.usr_move = ""

    def recommend_move(self):
        m = self.bot.get_best_move()
        self.b_list[btn_map[m[:2]]].configure(bg='#AFFFAF')
        self.b_list[btn_map[m[2:]]].configure(bg='#AFFFAF')

    def about(self):
        about_text = ''' 
        Developed by Rutuparn Pawar [InputBlackBoxOutput]

        Licensed under the MIT License
        '''
        msgbox.showinfo('About', about_text)

    def create_menu_bar(self):
        self.menu = Menu(self)
        self.menu.add_command(label='New game', command=self.new_game)
        self.menu.add_command(label='Recommend move',
                              command=self.recommend_move)
        self.menu.add_command(label='About', command=self.about)
        self.menu.add_command(label='Close', command=self.quit)

        self.config(menu=self.menu)

    # -------------------------------------------------------------------------------
    # Status bar

    def create_status_bar(self):
        self.status = Label(self, text="Developed by InputBlackBoxOutput",
                            font='calibri 12 normal', borderwidth=1, relief=SUNKEN, anchor='s', pady=4)
        self.status.pack(side=BOTTOM, fill=X)

        Label(window).pack(side=BOTTOM)  # Spacer

    # -------------------------------------------------------------------------------
    # Chessboard

    def create_chess_board(self, font, w, h):
        self.grid_map = Frame(window, bg='#AFAFAF', padx=1, pady=1)

        # Generate 64 button widgets
        self.b_list = []
        font = f"consolas {font} normal"

        for each in range(0, 64):
            self.b_list.append(Button(self.grid_map, text=' ', command=lambda each=each: self.on_button_click(
                each), font=font, width=w, height=h))

        # Place 64 button widgets in a 8x8 grid
        each = 0
        for r in range(0, 8):
            for c in range(0, 8):
                self.b_list[each].grid(row=r, column=c)

                if r % 2 != 0:
                    if each % 2 == 0:
                        self.b_list[each].configure(bg='#DFDFDF')
                else:
                    if each % 2 != 0:
                        self.b_list[each].configure(bg='#DFDFDF')
                each = each + 1

        self.grid_map.pack(side=BOTTOM)
        self.update_board()

    # -------------------------------------------------------------------------------
    # Chessboard helper functions

    def mark_move(self, move):
        m = str(move)
        self.b_list[btn_map[m[:2]]].configure(bg='#AFAFFF')
        self.b_list[btn_map[m[2:]]].configure(bg='#AFAFFF')

    def remove_marking(self):
        each = 0
        for r in range(0, 8):
            for c in range(0, 8):
                self.b_list[each].configure(bg='#F0F0F0')

                if r % 2 != 0:
                    if each % 2 == 0:
                        self.b_list[each].configure(bg='#DFDFDF')
                else:
                    if each % 2 != 0:
                        self.b_list[each].configure(bg='#DFDFDF')
                each = each + 1

    def position_has_white_piece(self, position):
        board_state = ""

        fen = self.bot.get_fen_position()
        for x in str(fen).split(" ")[0]:
            if x.isnumeric():
                for n in range(0, int(x)):
                    board_state += "-"
            else:
                if x != "/":
                    board_state += x

        if len(position) == 2:
            if board_state[btn_map[position]] in ['K', 'Q', 'R', 'B', 'N', 'P']:
                return True
            else:
                return False

    def check_endgame_conditions(self):
        fen = self.bot.get_fen_position()
        board = chess.Board(fen)

        c = None
        if board.is_check():
            c = "Check"
        if board.is_checkmate():
            c = "Checkmate"

        return c

    def on_button_click(self, button):
        self.remove_marking()
        self.status.configure(text="")

        if self.game_over == False:
            # Get row
            if button >= 0 and button <= 31:
                if button >= 0 and button <= 7:
                    r = 8
                if button >= 8 and button <= 15:
                    r = 7
                if button >= 16 and button <= 23:
                    r = 6
                if button >= 24 and button <= 31:
                    r = 5
            else:
                if button >= 32 and button <= 39:
                    r = 4
                if button >= 40 and button <= 47:
                    r = 3
                if button >= 48 and button <= 55:
                    r = 2
                if button >= 56 and button <= 63:
                    r = 1

            # Get column
            c = chr(97 + button % 8)

            if len(self.usr_move) == 2:
                self.remove_marking()
                self.usr_move += c + str(r)
                print(f"U: {self.usr_move}")

                if self.position_has_white_piece(self.usr_move[:2]) and self.position_has_white_piece(self.usr_move[2:]):
                    self.usr_move = self.usr_move[2:]
                    self.remove_marking()

                    self.b_list[btn_map[self.usr_move]].configure(bg='#FFFFAF')
                    return

                if self.bot.is_move_correct(self.usr_move):
                    self.bot.make_moves_from_current_position([self.usr_move])
                    self.usr_move = ""
                else:
                    self.status.config(text="Invalid move")
                    self.usr_move = ""
                    return

                self.update_board()

                # End game condition check
                c = self.check_endgame_conditions()
                if c == 'Check':
                    self.status.config(text=c)
                elif c == 'Checkmate':
                    self.game_over = True
                    self.status.config(text=c)
                    return

                # Computers turn
                best_move = self.bot.get_best_move()
                print(f"C: {best_move}\n")

                self.bot.make_moves_from_current_position([best_move])
                self.mark_move(best_move)
                self.update_board()

                # End game condition check
                c = self.check_endgame_conditions()
                if c == 'Check':
                    self.status.config(text=c)
                elif c == 'Checkmate':
                    self.game_over = True
                    self.status.config(text=c)
                    return

            else:
                self.usr_move += c + str(r)

                if(self.position_has_white_piece(self.usr_move)):
                    self.b_list[btn_map[self.usr_move]].configure(bg='#FFFFAF')
                else:
                    self.usr_move = ""

    def update_board(self):
        board_state = ""
        fen = self.bot.get_fen_position()

        # print(fen)
        for x in str(fen).split(" ")[0]:
            if x.isnumeric():
                for n in range(0, int(x)):
                    board_state += "-"
            else:
                if x != "/":
                    board_state += x

        # print(board_state)

        for i in range(64):
            self.b_list[i].configure(text=unicode_map[board_state[i]])


# -------------------------------------------------------------------------------------------
if __name__ == '__main__':
    print("Please minimize this window")
    os_name = platform.system().lower()

    if 'windows' in os_name:
        window = GUI(740, 680)
    else:
        window = GUI(700, 680)

    window.create_menu_bar()
    window.create_status_bar()

    if 'windows' in os_name:
        window.create_chess_board(18, 6, 2)
    else:
        window.create_chess_board(18, 4, 2)

    window.mainloop()

# -------------------------------------------------------------------------------------------
