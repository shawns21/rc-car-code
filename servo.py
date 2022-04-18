from gpiozero import Servo
from time import sleep
import math
import curses

from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

servo = Servo(17, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)

while True:
    direction = screen.getch()
    if direction == curses.KEY_RIGHT:
        servo.value = -1
    elif direction == curses.KEY_LEFT:
        servo.value = 1
