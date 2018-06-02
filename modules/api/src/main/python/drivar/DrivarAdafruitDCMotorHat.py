#  Driver library for Raspbuggy - Adafruit DC Motor Hat (i2c implementation)
'''
Created on Apr 24, 2016

@author: bcopy
'''

from drivar.Drivar import Drivar
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import RPi.GPIO as GPIO
import atexit
import time

GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 18

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)

class DrivarAdafruitDCMotorHat(Drivar):
    
    def __init__(self):
        self.initialized = False
        self.hat = Adafruit_MotorHAT(addr=0x60)

        self.motorOne =    None
        self.motorTwo =    None
        self.motorThree =  None
        self.motorFour =   None
        self.moving = False
        self.currentSpeed = 0
        self.leftCurrentDirection = None
        self.rightCurrentDirection = None


    def initialize(self):
        super(DrivarAdafruitDCMotorHat,self).initialize()
        self.motorOne =   self.hat.getMotor(1)
        self.motorTwo =   self.hat.getMotor(2)
        self.motorThree = self.hat.getMotor(3)
        self.motorFour =  self.hat.getMotor(4)
        self.leftMotors = [self.motorOne, self.motorFour]
        self.rightMotors = [self.motorTwo, self.motorThree]
        self.allMotors = [self.motorOne, self.motorTwo, self.motorThree,  self.motorFour]
        
        self.initialized = True
        atexit.register(self._shutdown)
        

    def move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, callback = None):
        if (self.moving) :
            self.stop()
        durationInMs = max(durationInMs,100)
        _direct = direction
        self.rotateWheels(direction = _direct)
        time.sleep(durationInMs/1000)
        self.stop()
        if callback is not None:
            callback()
    
    def rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speedLevel = Drivar.SPEED_FAST, callback = None):
        if (self.moving) :
            self.stop()
        power = self._getDCMotorHatSpeed(speedLevel)
        motorsToActuate = []
        
        if direction == Drivar.DIR_FORWARD:
            for m in self.allMotors:
                m.run(Adafruit_MotorHAT.FORWARD)
        elif direction == Drivar.DIR_BACKWARD:
            for m in self.allMotors:
                m.run(Adafruit_MotorHAT.BACKWARD)
        elif direction == Drivar.DIR_LEFT:
            for m in self.rightMotors:
                m.run(Adafruit_MotorHAT.FORWARD)
            for m in self.leftMotors:
                m.run(Adafruit_MotorHAT.BACKWARD)
        elif direction == Drivar.DIR_RIGHT:
            for m in self.leftMotors:
                m.run(Adafruit_MotorHAT.FORWARD)
            for m in self.rightMotors:
                m.run(Adafruit_MotorHAT.BACKWARD)
        
        motorsToActuate = self.allMotors
        
        self._actuateMotors(motorsToActuate, power)
        
        if callback is not None:
            callback()
        
    """
       Turn the wheels in the given direction to the given angle.
       Note that this class is using DC motors, so the resulting
       rotation angle is very imprecise and offers no guarantees.
    """
    def turn(self, direction = Drivar.DIR_LEFT, angle = 90, callback = None):
        if (direction == Drivar.DIR_PORTSIDE or direction == Drivar.DIR_LEFT):
            for m in self.rightMotors:
                m.run(Adafruit_MotorHAT.FORWARD)
            for m in self.leftMotors:
                m.run(Adafruit_MotorHAT.BACKWARD)
        elif (direction == Drivar.DIR_STARBOARD or direction == Drivar.DIR_RIGHT):
            for m in self.leftMotors:
                m.run(Adafruit_MotorHAT.FORWARD)
            for m in self.rightMotors:
                m.run(Adafruit_MotorHAT.BACKWARD)
        
        motorsToActuate = self.allMotors
        self._actuateMotors(motorsToActuate, self._getDCMotorHatSpeed(Drivar.SPEED_MEDIUM))
        time.sleep( (angle/90) * 0.9 )
        self.stop()
        
        if callback is not None:
            callback()

    """ 
       Internal method to ramp up the speed of the given list of motors
       to a target power level
    """
    def _actuateMotors(self, motorsToActuate, power):
        self.moving = True
        for x in range(power, 20):
            for motor in motorsToActuate:
                motor.setSpeed(x)
                time.sleep(0.01)
        for motor in motorsToActuate:
                motor.setSpeed(power)        
        self.currentSpeed = power
    
    """
      Brings all the motors to a stop (ramp down the speed quickly if
      the motors are currently running)
    """
    def stop(self, callback = None):
        if self.moving :
            for x in range(self.currentSpeed, 0, -20):
                for m in self.allMotors:
                    m.setSpeed(x)
                    time.sleep(0.01)
        for m in self.allMotors:
            m.run(Adafruit_MotorHAT.RELEASE)
        time.sleep(0.1)
        self.moving = False
        if callback is not None:
                callback()
        
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def getDistanceToObstacle(self):
        GPIO.output(TRIG, False)
        time.sleep(1)
    	GPIO.output(TRIG, True)
    	time.sleep(0.00001)
    	GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        return distance

    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def isObstacleWithin(self, distance):
        return (self.getDistanceToObstacle() <= distance)
    
    def rotatePen(self, angle):
        pass

    def getReflectivityMeasurement(self):
        return 0
        
    def wait(self, milliseconds):
        time.sleep(milliseconds/1000)

    def _shutdown(self):
        self.stop()
        GPIO.cleanup()


    '''
      Return the Adafruit Motor HAT speed equivalent for the given DRIVAR speed flag
    '''
    @staticmethod
    def _getDCMotorHatSpeed(speed):
        if(speed==Drivar.SPEED_SLOW):
            return 75
        elif(speed==Drivar.SPEED_MEDIUM):
            return 200
        elif(speed==Drivar.SPEED_FAST):
            return 255
        else :
            return 75

Drivar.register(DrivarAdafruitDCMotorHat)

if __name__ == '__main__':
    _drivar = DrivarAdafruitDCMotorHat()
