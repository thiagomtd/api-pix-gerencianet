import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)  # desativa sinalização de pino em uso
# RuntimeWarning: This channel is already in use, continuing anyway.
# Use GPIO.setwarnings(False) to disable warnings.


def init():  # Configurar GPIO com base nos pinos da Ponte-H
    GPIO.setmode(GPIO.BOARD)  # Declare a configuração GPIO
    GPIO.setup(22, GPIO.OUT)  # Conectado no pino ENA 22/40 GPIO 25
    GPIO.setup(18, GPIO.OUT)  # Conectado no pino IN1 18/40      23
    GPIO.setup(16, GPIO.OUT)  # Conectado no pino IN2 16/40      24
    GPIO.setup(11, GPIO.OUT)  # Conectado no pino IN3 11/40      17
    GPIO.setup(13, GPIO.OUT)  # Conectado no pino IN4 13/40      27
    GPIO.setup(15, GPIO.OUT)  # Conectado no pino ENB 15/40      22


def reset():  # Reset all the GPIO pins by setting them to LOW
    GPIO.output(22, GPIO.LOW)  # Set AIN1
    GPIO.output(18, GPIO.LOW)  # Set AIN2
    GPIO.output(16, GPIO.LOW)  # Set PWMA
    GPIO.output(11, GPIO.LOW)  # Set BIN1
    GPIO.output(13, GPIO.LOW)  # Set BIN2
    GPIO.output(15, GPIO.LOW)  # Set PWMB


def motor1(quantidade):  # Girar sentido horário por t segundos com potencia d
    init()
    GPIO.output(18, GPIO.HIGH)  # Set AIN1
    GPIO.output(16, GPIO.LOW)   # Set AIN2
    # velocidade do motor
    PWMA = GPIO.PWM(15, 100)  # Com PWM
    PWMA.start(60)
    time.sleep(1*quantidade)
    PWMA.stop()
    reset()


def motor2(quantidade):  # Girar sentido horário por t segundos com potencia d
    init()
    GPIO.output(11, GPIO.HIGH)  # Set BIN1
    GPIO.output(13, GPIO.LOW)  # Set BIN2
    # velocidade do motor
    PWMB = GPIO.PWM(15, 100)  # Com PWM
    PWMB.start(60)
    time.sleep(1 * quantidade)
    PWMB.stop()
    reset()
