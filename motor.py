from pynput import keyboard
import os
from gpiozero import Servo
import time
import math
from gpiozero.pins.pigpio import PiGPIOFactory
os.system ("sudo pigpiod")

factory = PiGPIOFactory()

servo = Servo(21, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)

test = 0.00

def on_press(key):

    global test
   
    if key == keyboard.Key.up:
        while test < 0.95:
            test = test + 0.02
            servo.value = test
            time.sleep(0.01)
            print (servo.value)
            break


    if key == keyboard.Key.down:
        while test > -0.95:
            test = test - 0.02
            servo.value = test
            time.sleep(0.01)
            print (servo.value)
            break



        
def on_release(key):
    
    global test

    test = 0.00
    servo.value = test


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

test = 0
servo.value = 0
