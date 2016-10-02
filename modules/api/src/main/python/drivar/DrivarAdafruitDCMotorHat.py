#  Driver library for Raspbuggy - Adafruit DC Motor Hat (i2c implementation)
'''
Created on Apr 24, 2016

@author: bcopy
'''

from drivar.Drivar import Drivar
from Adafruit_MotorHAT import Adafruit_MotorHAT, Adafruit_DCMotor

import pytweening

import atexit
import time

class DrivarAdafruitDCMotorHat(Drivar):
    
    def __init__(self):
        self.m_initialized = False
        self.mh = Adafruit_MotorHAT(addr=0x60)

        self.m_frontLeftMotor = None
        self.m_frontRightMotor = None
        self.m_backLeftMotor = None
        self.m_backRightMotor = None
        self.m_moving = False
        self.m_currentSpeed = 0
        self.m_leftCurrentDirection = None
        self.m_rightCurrentDirection = None


    def initialize(self):
        super(DrivarAdafruitDCMotorHat,self).initialize()
        self.m_frontLeftMotor = mh.getMotor(1)
        self.m_frontRightMotor = mh.getMotor(2)
        self.m_backRightMotor = mh.getMotor(3)
        self.m_backLeftMotor = mh.getMotor(4)
        self.m_leftMotors = [self.m_frontLeftMotor, self.m_backLeftMotor]
        self.m_rightMotors = [self.m_frontRightMotor, self.m_backRightMotor]
        self.m_allMotors = [self.m_frontLeftMotor, self.m_frontRightMotor, self.m_backRightMotor,  self.m_backLeftMotor]
        self.m_initialized = True
        atexit.register(self.stop)

    def move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, callback = None):
        durationInMs = max(durationInMs,100)
        _direct = direction
        self.rotateWheels(direction = _direct)
        time.sleep(durationInMs/1000)
        self.stop()
        if callback is not None:
            callback()
    
    
    """
      Internal method to control wheel rotation - the speed updates must be gradual to
      obtain the best movement precision possible.
    """
    def _updateWheelsRotation(self, leftSetDirection = Drivar.DIR_FORWARD, rightSetDirection = Drivar.DIR_FORWARD, newDcMotorHatSpeed, callback = None):
        # Work out the steps required to affect speed differences between the current speed and the future one
        leftReverseDirection = False
        if(self.m_leftCurrentDirection != leftSetDirection):
            leftReverseDirection = True
        
        leftSteps = [ ]
        leftSpeedStart = ( ( -1 * self.m_currentSpeed ) if (m_leftCurrentDirection == Drivar.DIR_BACKWARD) else self.m_currentSpeed)
        leftSpeedEnd = newDcMotorHatSpeed
        
        
        # Step 2, work out ten steps that will bring our current speed to the required level
        distance = abs(newSpeed - self.m_currentSpeed)
        for x in range(1.1,0.1):
            steps.append(pytweening.easeInOutCubic(x) * distance)
        
        # Step 2 bis, if we are decelerating, we simply reverse the sequence
        if(not(accelerating)):
            steps = steps.reverse()
        
        # Step 3, update the motors with their required direction
        
        
        # Apply the speed change steps
        for i in range(SPEED):
            Motor.setSpeed(SPEED)
            time.sleep(0.01)
            self.m_frontLeftMotor.run(power)
            self.m_backLeftMotor.run(power)
        if(wheelSet == Drivar.WHEELS_RIGHT or wheelSet == Drivar.WHEELS_BOTH):
            self.m_frontRightMotor.run(power)
            self.m_backRightMotor.run(power)
        self.m_moving = True
        if callback is not None:
            callback()

  def rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speedLevel = Drivar.SPEED_FAST, callback = None):
        speed = self._getDCMotorHatSpeed(speedLevel)
        motorHatDirection = Adafruit_MotorHAT.FORWARD
        if(direction == Drivar.DIR_BACKWARD):
            motorHatDirection = Adafruit_MotorHAT.BACKWARD
        motorControlSet = []
        # Determine how many wheels we must affect
        if(wheelSet == Drivar.WHEELS_BOTH):
            motorControlSet = self.m_allMotors
        if(wheelSet == Drivar.WHEELS_LEFT):
            motorControlSet = self.m_leftMotors
        if(wheelSet == Drivar.WHEELS_RIGHT):
            motorControlSet = self.m_rightMotors
        
        for i in range(SPEED):
            Motor.setSpeed(SPEED)
            time.sleep(0.01)
            self.m_frontLeftMotor.run(power)
            self.m_backLeftMotor.run(power)
        if(wheelSet == Drivar.WHEELS_RIGHT or wheelSet == Drivar.WHEELS_BOTH):
            self.m_frontRightMotor.run(power)
            self.m_backRightMotor.run(power)
        self.m_moving = True
        if callback is not None:
            callback()
        
    def turn(self, direction = Drivar.DIR_LEFT, angle = 90, callback = None):
        left_power = -100
        right_power = 100
        if(direction == Drivar.DIR_RIGHT):
            left_power *= -1 
            right_power *= -1
        # TODO : Complete implementation
        self.m_frontRightMotor.turn(left_power, angle)
        self.m_rightMotor.turn(right_power, angle)


    
    
    def stop(self, callback = None):
        if(self.m_moving):
            for i in reversed(range(self.m_currentSpeed)):
                for m in self.m_allMotors:
                    m.setSpeed(i)
                time.sleep(0.01)
         for m in self.m_allMotors:
             m.run(Adafruit_MotorHAT.RELEASE)
         self.m_moving = False
         self.m_currentSpeed = 0
            if callback is not None:
                callback()
 
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def getDistanceToObstacle(self):
        # TODO : Add ultrasonic sensor support
        return 200
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def isObstacleWithin(self, distance):
        # TODO : Add ultrasonic sensor support
        return False
    
    def rotatePen(self, angle):
        pass

    def getReflectivityMeasurement(self):
        return 0
        
    def wait(self, milliseconds):
        time.sleep(milliseconds/1000)

    '''
      Return the Adafruit Motor HAT speed equivalent for the given DRIVAR speed flag
    '''
    @staticmethod
    def _getDCMotorHatSpeed(speed):
        if(speed==Drivar.SPEED_SLOW):
            return 150
        elif(speed==Drivar.SPEED_MEDIUM):
            return 200
        elif(speed==Drivar.SPEED_FAST):
            return 255
        else :
            return 150 

Drivar.register(DrivarAdafruitDCMotorHat)

if __name__ == '__main__':
    _drivar = DrivarAdafruitDCMotorHat()
