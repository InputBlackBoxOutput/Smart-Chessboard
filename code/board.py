import time
from connections import D_S0, D_S1, D_S2, M_S0, M_S1, M_S2, M_OUT

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)  # Use GPIO numbers
GPIO.setwarnings(False)

# ---------------------------------------------------------------------------------


class Board():
    def __init__(self):
        self.demux_select_lines = [D_S0, D_S1, D_S2]
        GPIO.setup(D_S0, GPIO.OUT)
        GPIO.setup(D_S1, GPIO.OUT)
        GPIO.setup(D_S2, GPIO.OUT)

        self.mux_select_lines = [M_S0, M_S1, M_S2]
        GPIO.setup(M_S0, GPIO.OUT)
        GPIO.setup(M_S1, GPIO.OUT)
        GPIO.setup(M_S2, GPIO.OUT)
        GPIO.setup(M_OUT, GPIO.IN)

        # Check at initialization
        self.previous_board_state = [[1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [0, 0, 0, 0, 0, 0, 0],
                                     [1, 1, 1, 1, 1, 1, 1],
                                     [1, 1, 1, 1, 1, 1, 1]]

        self.board_state = [[1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0],
                            [1, 1, 1, 1, 1, 1, 1],
                            [1, 1, 1, 1, 1, 1, 1]]

    # Set select lines of MUX/DEMUX
    def set_select_lines(self, select_lines, n):
        b = bin(n).split('b')[1]
        if len(b) == 1:
            b = "00" + b
        elif len(b) == 2:
            b = "0" + b

        for i in range(3):
            if b[i] == '1':
                GPIO.output(select_lines[i], GPIO.HIGH)
            else:
                GPIO.output(select_lines[i], GPIO.LOW)

    # Scan the board using MUX and DEMUX logic

    def get_board_state(self):
        self.previous_board_state = self.board_state.copy()

        for d in range(8):
            self.set_select_lines(self.demux_select_lines, d)
            for m in range(8):
                self.set_select_lines(self.mux_select_lines, m)

                # Hall effect sensor output gets low when a magnet is nearby
                if GPIO.input(M_OUT) == False:
                    self.board_state[m][d] = 1
                else:
                    self.board_state[m][d] = 0

                time.sleep(0.1)

    # Find difference between present board state and previous board state to find move
    def find_move(self):
        change = [None, None, None, None]

        for d in range(8):
            for m in range(8):
                if self.previous_board_state[m][d] != self.board_state[m][d]:
                    if self.board_state[m][d] == 0:
                        change[0] = m
                        change[1] = d
                    else:
                        change[2] = m
                        change[3] = d

            # Stop scan if found
            if None not in change:
                break

        # Player did not make a move
        if None in change:
            return None

        # Return the move in uci format
        map = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h'}

        return map[change[0]] + str(change[1] + 1) + map[change[2]] + str(change[3] + 1)

    def __del__(self):
        GPIO.cleanup()


# ---------------------------------------------------------------------------------
if __name__ == "__main__":
    board = Board()

    # Check to see if all pieces are detected
    board.get_board_state()
    print(board.board_state)

# ---------------------------------------------------------------------------------
