# Smart chessboard
# Written by Rutuparn Pawar [InputBlackBoxOutput]

# Stockfish source: https://github.com/well69/Chess-Engines-for-Raspberry-Pi-by-Al
# Use compiled executable from 'arm6l' directory for Raspberry Pi Zero


# TODO
# Setup logging using logging module
# Setup UART (See AUX connector) to connect with stepper motor board (To be designed)

import time
import chess
from stockfish import Stockfish

from board import Board
from buttons import Button
from buzzer import Buzzer
from rgb_led import Neopixels
from stat_led import StatLED


from connections import BTN1, BTN2, BTN3, BTN4

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # Use GPIO numbers
GPIO.setwarnings(False)


def test_interface(btn, stat, buzz):
    print("Interface test")

    if btn.button_pressed(BTN1) or btn.button_pressed(BTN2):
        stat.blink()

    if btn.button_pressed(BTN3) or btn.button_pressed(BTN4):
        buzz.sound_buzzer()


# ---------------------------------------------------------------------------------
# Colours
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# ---------------------------------------------------------------------------------


def main():
    board = Board()
    btn = Button()
    buzz = Buzzer()
    pixels = Neopixels()
    stat = StatLED()

    bot = Stockfish(r"stockfish/stockfish")
    game_over = False

    while(1):
        pixels.clear()
        stat.blink()

        if btn.button_pressed(BTN1):
            bot.set_fen_position(
                "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
            game_over = False
            pixels.clear()

        if btn.button_pressed(BTN2):
            # Recommend move
            m = bot.get_best_move()
            pixels.set_pixel_at_position(m[:2], GREEN)
            pixels.set_pixel_at_position(m[2:], GREEN)

            time.delay(3)

        # Extra buttons: Use to play tetris on the board :-)
        if btn.button_pressed(BTN3):
            pass

        if btn.button_pressed(BTN3):
            pass

        if game_over == False:
            # Find user move and play it in the chess engine
            usr_move = board.find_move()
            if usr_move == None:
                continue

            print(f"U: {usr_move}\n")

            pixels.set_pixel_at_position(usr_move[:2], YELLOW)
            pixels.set_pixel_at_position(usr_move[2:], YELLOW)

            if bot.is_move_correct(usr_move):
                bot.make_moves_from_current_position([usr_move])
            else:
                print("Invalid move")
                buzz.sound_buzzer()

            # Check for endgame conditions
            fen = bot.get_fen_position()
            board = chess.Board(fen)

            if board.is_check():
                buzz.sound_buzzer()
            if board.is_checkmate():
                buzz.sound_buzzer()
                time.sleep(0.5)
                buzz.sound_buzzer()
                game_over = True

            # Computers turn
            best_move = bot.get_best_move()
            print(f"C: {best_move}\n")

            pixels.set_pixel_at_position(best_move[:2], BLUE)
            pixels.set_pixel_at_position(best_move[2:], BLUE)

            bot.make_moves_from_current_position([best_move])

            # Check for endgame conditions
            fen = bot.get_fen_position()
            board = chess.Board(fen)

            if board.is_check():
                buzz.sound_buzzer()
            if board.is_checkmate():
                buzz.sound_buzzer()
                time.sleep(0.2)
                buzz.sound_buzzer()
                game_over = True

        time.sleep(0.5)

    # Uncomment for testing
    # while(1):
    #     test_interface(btn, stat, buzz)


# ---------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

# ---------------------------------------------------------------------------------
