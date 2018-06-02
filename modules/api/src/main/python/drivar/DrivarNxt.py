#  Driver library for Raspbuggy - Lego py-nxt implementation
'''
Created on Mar 18, 2015

@author: bcopy
'''

import nxt.locator
from nxt.motor import Motor,PORT_A,PORT_B,PORT_C
from nxt.sensor import Ultrasonic,Light,PORT_1,PORT_2,PORT_3,PORT_4

from drivar.Drivar import Drivar
import time

class DrivarNxt(Drivar):
    
    def __init__(self):
        self.initialized = False
        self.block = None
        self.leftMotor = None
        self.rightMotor = None
        self.penMotor = None
        self.ultrasonicSensor = None
        self.lightSensor = None
        self.moving = False

    def initialize(self):
        super(DrivarNxt,self).initialize()
        self.block = nxt.locator.find_one_brick()
        self.leftMotor = Motor(self.block, PORT_A)
        self.rightMotor = Motor(self.block, PORT_C)
        self.penMotor = Motor(self.block, PORT_B)
        self.ultrasonicSensor = Ultrasonic(self.block, PORT_4)
        self.lightSensor = Light(self.block, PORT_3)
        self.initialized = True
        

    def motor_move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, speed = Drivar.SPEED_SLOW, callback = None):
        durationInMs = max(durationInMs,100)
        _direct = direction
        self.rotateWheels(direction = _direct)
        time.sleep(durationInMs/1000)
        self.stop()
        if callback is not None:
            callback()
    
    def motor_rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speed = Drivar.SPEED_SLOW, callback = None):
        power = self._getNxtSpeed(speedLevel)
        # Correct the power (positive vs negative) depending on the direction
        if(direction == Drivar.DIR_FORWARD):
            if(power < 0):
                power = power * -1
        if(direction == Drivar.DIR_BACKWARD):
            if(power > 0):
                power = power * -1
        # Get the wheels turning
        if(wheelSet == Drivar.WHEELS_LEFT or wheelSet == Drivar.WHEELS_BOTH):
            self.leftMotor.run(power)
        if(wheelSet == Drivar.WHEELS_RIGHT or wheelSet == Drivar.WHEELS_BOTH):
            self.rightMotor.run(power)
        self.moving = True
        if callback is not None:
            callback()
        
    def motor_turn(self, direction = Drivar.DIR_LEFT, angle = 90, callback = None):
        left_power = -100
        right_power = 100
        if(direction == Drivar.DIR_RIGHT):
            left_power *= -1 
            right_power *= -1
        self.leftMotor.turn(left_power, angle)
        self.rightMotor.turn(right_power, angle)


    
    
    def motor_stop(self, callback = None):
        self.leftMotor.idle()
        self.rightMotor.idle()
        self.moving = False
        if callback is not None:
            callback()
        
 
 
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def range_getDistanceToObstacle(self):
        return self.ultrasonicSensor.get_sample()
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def range_isObstacleWithin(self, distance):
        dist = self.ultrasonicSensor.get_sample()
        if(dist <= distance):
            return True
        else:
            return False
    
    def pen_rotate(self, angle):
        power = 70
        if angle < 0:
            angle = -1 * angle
            power = -70
        self.penMotor.turn(power, angle)

    def reflectivity_get(self):
        self.lightSensor.set_illuminated(True)
        return self.lightSensor.get_sample()
        
    '''
      Return the NXT speed equivalent for the given DRIVAR speed flag
    '''
    @staticmethod
    def _getNxtSpeed(speed):
        if(speed==Drivar.SPEED_SLOW):
            return 70
        elif(speed==Drivar.SPEED_MEDIUM):
            return 100
        elif(speed==Drivar.SPEED_FAST):
            return 127
        else :
            return 100 

Drivar.register(DrivarNxt)

if __name__ == '__main__':
    _drivar = DrivarNxt()
