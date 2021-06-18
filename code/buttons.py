from time import sleep
from connections import BTN1, BTN2, BTN3, BTN4

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ---------------------------------------------------------------------------------


class Button():
    def __init__(self, debounce_time=0.2):
        GPIO.setup(BTN1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BTN2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BTN3, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(BTN4, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.debounce_time = debounce_time

    def button_pressed(self, BTN):
        if GPIO.input(BTN) == False:
            sleep(self.debounce_time)

            if GPIO.input(BTN) == False:
                return True
            else:
                return False

    def __del__(self):
        GPIO.cleanup()


# ---------------------------------------------------------------------------------
if __name__ == "__main__":
    btn = Button()
    if btn.button_pressed(BTN1):
        print("Button pressed")

# ---------------------------------------------------------------------------------
