from drivar.Drivar import Drivar
from drivar.DrivarHolonomic import DrivarHolonomic
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(18, 50)  # channel=12 frequency=50Hz
p.start(0)
p.ChangeDutyCycle(100)


drivar = DrivarHolonomic()
drivar.initialize()

#drivar.motor_move(Drivar.DIR_BACKWARD)
#drivar.motor_turn(Drivar.DIR_RIGHT, 90)



