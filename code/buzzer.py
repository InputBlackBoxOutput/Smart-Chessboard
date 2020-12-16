from time import sleep
from connections import BUZZ

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#---------------------------------------------------------------------------------
class Buzzer:
    def __init__(self):
        GPIO.setup(BUZZ, GPIO.OUT)

    def sound_buzzer(self, duration=0.5):
        GPIO.output(BUZZ, GPIO.HIGH)
        sleep(duration)
        GPIO.output(BUZZ, GPIO.LOW)
    
    def __del__(self):
        GPIO.cleanup()


#---------------------------------------------------------------------------------
if __name__ == "__main__":
    buzz = Buzzer()
    buzz.sound_buzzer()
    # buzz.sound_buzzer(2)

#---------------------------------------------------------------------------------
