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

drivar.motor_move(Drivar.DIR_BACKWARD, 1200)
drivar.motor_turn(Drivar.DIR_LEFT, 90)
drivar.motor_move(Drivar.DIR_BACKWARD, 1900)
drivar.motor_turn(Drivar.DIR_LEFT, 360)
drivar.motor_move(Drivar.DIR_BACKWARD, 1900)
drivar.motor_turn(Drivar.DIR_RIGHT, 90)
drivar.time_wait(3000)
drivar.motor_move(Drivar.DIR_BACKWARD, 2000)
drivar.motor_turn(Drivar.DIR_LEFT, 360)
drivar.motor_move(Drivar.DIR_BACKWARD, 2000)
drivar.motor_turn(Drivar.DIR_RIGHT, 90)
drivar.time_wait(3000)
drivar.motor_move(Drivar.DIR_BACKWARD, 2000)
drivar.motor_turn(Drivar.DIR_LEFT, 360)
drivar.motor_move(Drivar.DIR_BACKWARD, 1800)
drivar.motor_turn(Drivar.DIR_RIGHT, 90)
drivar.time_wait(3000)
drivar.motor_move(Drivar.DIR_BACKWARD, 2000)
drivar.motor_turn(Drivar.DIR_LEFT, 360)
drivar.motor_move(Drivar.DIR_BACKWARD, 2500)
drivar.motor_turn(Drivar.DIR_RIGHT, 180)


p.stop()
GPIO.cleanup()
#drivar.motor_turn(Drivar.DIR_RIGHT, 90)



