from gpiozero import Motor
import time

motor = Motor(forward=20, backward=21)

while True:
    print('Forward')
    motor.forward(1)
    time.sleep(5)
    print('Backward')
    motor.Backward(1)
    time.sleep(5)
    
