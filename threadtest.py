import os
os.system("sudo pigpiod")
import pygame
import sys
from gpiozero import Servo
import math
from gpiozero.pins.pigpio import PiGPIOFactory
import time
import threading

factory = PiGPIOFactory()

servo = Servo(13, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)
motor = Servo(21, min_pulse_width = 0.5 / 1000, max_pulse_width = 2.5 / 1000, pin_factory = factory)


motor.value = 0.00
servo.value = 0.00

pygame.init()
display = pygame.display.set_mode((100, 100))



def listenServo():
    
    glint = False
   
    while True:
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == pygame.K_LEFT:
                    glint = True 
            
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_LEFT:
                    glint = False
                    servo.value = 0.00

        if glint:
            if servo.value < 0.95:
                servo.value = servo.value + 0.02
                time.sleep(0.01)
                print(servo.value)


def listenMotor():

    wint = False
   
    while True:
    
        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            
                if event.key == pygame.K_UP:
                    wint = True
             
            if event.type == pygame.KEYUP:

                if event.key == pygame.K_UP:
                    wint = False
                    motor.value = 0.00

        if wint:
            if motor.value < 0.95:
                motor.value = motor.value + 0.02
                time.sleep(0.01)
                print(motor.value)

        
threading.Thread(target=listenServo).start()
threading.Thread(target=listenMotor).start()






