import os
os.system("sudo pigpiod")
import pygame
import sys
from gpiozero import Servo
import math
from gpiozero.pins.pigpio import PiGPIOFactory
import time
from pygame.locals import *

factory = PiGPIOFactory()

servo = Servo(13, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)
motor = Servo(21, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)


motor.value = 0.00
servo.value = 0.00

pygame.init()
display = pygame.display.set_mode((800, 800))


west = False


while not west:

    pressed = pygame.key.get_pressed()
        
    for event in pygame.event.get():
        if pressed[pygame.K_ESCAPE]:
            west = True
   
    if pressed[K_LEFT] and pressed[K_UP]:
        if servo.value < 0.95:
            servo.value = servo.value + 0.02
            time.sleep(0.01)
        if motor.value < 0.95:
            motor.value = motor.value + 0.02
            time.sleep(0.01)

             
    elif pressed[K_LEFT] and pressed[K_DOWN]:
        if servo.value < 0.95:
            servo.value = servo.value + 0.02
            time.sleep(0.01)

        if motor.value > -0.95:
            motor.value = motor.value - 0.02
            time.sleep(0.01)

    
    elif pressed[K_RIGHT] and pressed[K_UP]:
        if servo.value > -0.95:
            servo.value = servo.value - 0.02
            time.sleep(0.01)

        if motor.value < 0.95:
            motor.value = motor.value + 0.02
            time.sleep(0.01)

   
    elif pressed[K_RIGHT] and pressed[K_DOWN]:
        if servo.value > -0.95:
            servo.value = servo.value - 0.02
            time.sleep(0.01)

        if motor.value > -0.95:
            motor.value = motor.value - 0.02
            time.sleep(0.01)

    
    elif pressed[K_LEFT]:
        if servo.value < 0.95:
            servo.value = servo.value + 0.02
            time.sleep(0.01)

    elif pressed[K_RIGHT]:
        if servo.value > -0.95:
            servo.value = servo.value - 0.02
            time.sleep(0.01)
            
    elif pressed[K_UP]:
        if motor.value < 0.95:
            motor.value = motor.value + 0.02
            time.sleep(0.01)

    elif pressed[K_DOWN]:
        if motor.value > -0.95:
            motor.value = motor.value - 0.02
            time.sleep(0.01)

    else:
        servo.value = 0.00
        motor.value = 0.00
 


