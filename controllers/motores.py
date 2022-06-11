from gpiozero import Motor
from time import sleep


def motor2(tempo):
    motor2 = Motor(22,23)
    motor2.backward() 

    sleep(tempo)        
    motor2.stop()




def motor1(tempo):
    motor1 = Motor(17,27)

    motor1.forward()

    sleep(tempo)        
    motor1.stop()
