from gpiozero import Servo
import time
from time import sleep
import math
from gpiozero.pins.pigpio import PiGPIOFactory
import curses

factory = PiGPIOFactory()


servo = Servo(17, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

servo.value = 0.00

while True:
    char = screen.getch()

    if char == curses.KEY_RIGHT:
        while servo.value > -0.95:
            servo.value = servo.value - 0.05
            break


    elif char == curses.KEY_LEFT:
        while servo.value < 0.95:
            servo.value = servo.value + 0.05
            break

