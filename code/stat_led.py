from time import sleep
from connections import STAT_LED

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#---------------------------------------------------------------------------------
class StatLED:
    def __init__(self):
        GPIO.setup(STAT_LED, GPIO.OUT)  # Setup stat as output

    def blink(self, times=3, delay=0.5):
    # Turn on stat led, wait for <delay> sec and then turn it off for <times> times
        for _ in range(times):
            GPIO.output(STAT_LED, GPIO.HIGH)
            sleep(delay)
            GPIO.output(STAT_LED, GPIO.LOW)

    def __del__(self):
        GPIO.cleanup()

#---------------------------------------------------------------------------------
if __name__ == "__main__":
    stat = StatLED()
    stat.blink()
    # stat.blink(5, 1) # Five times with one sec delay

#---------------------------------------------------------------------------------
