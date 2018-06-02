#  Driver library for Raspbuggy - Noop implementation for simulation and testing
'''
Created on Jun 01, 2015

@author: bcopy
'''

from drivar.Drivar import Drivar
import time
import logging

class DrivarNoop(Drivar):
    
    def __init__(self, enforceSleepingTime=False):
        self.initialized = False
        self.moving = False
        self.logger = logging.getLogger(__name__)
        self.enforceSleepingTime = enforceSleepingTime
        self.distanceToNextObstacle = 2000

    def initialize(self):
        super(DrivarNoop,self).initialize()
        self.logger.debug("Drivar : initialized")
        self.initialized = True
        

    def motor_move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, speed = Drivar.SPEED_SLOW, callback = None):
        durationInMs = max(durationInMs,100)
        _direct = direction
        _speed = speed
        self.motor_rotateWheels(direction = _direct, speed = _speed)
        self.wait(durationInMs/1000)
        self.motor_stop()
        if callback is not None:
            callback()
    
    def motor_rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speed = Drivar.SPEED_SLOW, callback = None):
        power = self._getMotorPowerLevel(speed)
        # Correct the power (positive vs negative) depending on the direction
        if(direction == Drivar.DIR_FORWARD):
            if(power < 0):
                power = power * -1
        if(direction == Drivar.DIR_BACKWARD):
            if(power > 0):
                power = power * -1
        # Get the wheels turning
        wheelSet = 'all'
        if(wheelSet == Drivar.WHEELS_LEFT):
            wheelSet = 'left'
        if(wheelSet == Drivar.WHEELS_RIGHT):
            wheelSet = 'right'
        
        self.logger.info("Drivar : Moving %s wheels with power %d.", wheelSet,power)
        self.moving = True
        if callback is not None:
            callback()
        
    def motor_turn(self, direction = Drivar.DIR_LEFT, angle = 90, callback = None):
        _dir = "left"
        if(direction == Drivar.DIR_RIGHT):
            _dir = "right"
        self.logger.info("Drivar : Turning the vehicle %s by %d degrees.",_dir,angle)
        self.wait(0.5)
        if callback is not None:
            callback()
    
    def motor_stop(self, callback = None):
        self.moving = False
        self.logger.info("Drivar : Stopping the vehicle.")
        if callback is not None:
            callback()
 
    def range_setDistanceToObstacle(self, distance):
        self.logger.info("Drivar : Set distance to next obstacle : %d cm", distance)
        self.distanceToNextObstacle = distance
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def range_getDistanceToObstacle(self):
        self.logger.info("Drivar : Getting distance to obstacle.")
        return self.distanceToNextObstacle
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def range_isObstacleWithin(self, distance):
        self.logger.debug("Drivar : Measuring whether obstacle is within %d cms", distance)
        dist = self.distanceToNextObstacle
        if(dist <= distance):
            self.logger.info("Drivar : Obstacle found within %d cms", distance)
            return True
        else:
            self.logger.info("Drivar : Obstacle NOT found within %d cms", distance)
            return False
    
    def pen_rotate(self, angle):
        self.logger.info("Drivar : Rotating the pen by %d degrees", angle)

    def reflectivity_get(self):
        return 150
        #return self.lightSensor.get_sample()
        
    def time_wait(self, milliseconds):
        if(self.enforceSleepingTime):
            time.sleep(milliseconds/1000)

    '''
      Return the NXT speed equivalent for the given DRIVAR speed flag
    '''
    @staticmethod
    def _getMotorPowerLevel(speed):
        if(speed==Drivar.SPEED_SLOW):
            return 70
        elif(speed==Drivar.SPEED_MEDIUM):
            return 100
        elif(speed==Drivar.SPEED_FAST):
            return 127
        else :
            return 100 

Drivar.register(DrivarNoop)

if __name__ == '__main__':
    _drivar = DrivarNoop()
