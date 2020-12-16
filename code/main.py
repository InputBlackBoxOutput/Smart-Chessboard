from buttons import Button
from stat_led import StatLED
from buzzer import Buzzer
from connections import BTN1, BTN2, BTN3, BTN4

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # Use GPIO numbers
GPIO.setwarnings(False) 


def test_interface(btn, stat, buzz):
    print("Interface test")

    if btn.button_pressed(BTN1) or btn.button_pressed(BTN2):
        stat.blink()
        
    if btn.button_pressed(BTN3) or btn.button_pressed(BTN4):
        buzz.sound_buzzer()

#---------------------------------------------------------------------------------
def main():
    btn = Button()
    stat = StatLED()
    buzz = Buzzer()
    while(1):
        test_interface(btn, stat, buzz)

    
#---------------------------------------------------------------------------------
if __name__ == "__main__":
    main()

#---------------------------------------------------------------------------------
