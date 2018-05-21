#  Driver library for Raspbuggy - Threejs / Brython implementation for simulation and testing
'''
Created on Jun 01, 2015

@author: bcopy
'''

from drivar.Drivar import Drivar
import time
import logging

class DrivarThreejs(Drivar):
    
    def __init__(self, enforceSleepingTime=False):
        self.m_initialized = False
        self.m_moving = False
        self.m_enforceSleepingTime = enforceSleepingTime
        self.m_distanceToNextObstacle = 2000

    def initialize(self):
        super(DrivarThreejs,self).initialize()
        print("Drivar : initialized")
        self.m_initialized = True
        

    def move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, callback = None):
        durationInMs = max(durationInMs,100)
        _direct = direction
        self.rotateWheels(direction = _direct)
        if(self.m_enforceSleepingTime):
            time.sleep(durationInMs/1000)
        self.stop()
        if callback is not None:
            callback()
    
    def rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speedLevel = Drivar.SPEED_FAST, callback = None):
        power = self._getNxtSpeed(speedLevel)
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
        
        print("Drivar : Moving %s wheels with power %d.", wheelSet,power)
        self.m_moving = True
        if callback is not None:
            callback()
        
    def turn(self, direction = Drivar.DIR_LEFT, angle = 90, callback = None):
        _dir = "left"
        if(direction == Drivar.DIR_RIGHT):
            _dir = "right"
        print("Drivar : Turning the vehicle %s by %d degrees.",_dir,angle)
        if(self.m_enforceSleepingTime):
            time.sleep(0.5)
        if callback is not None:
            callback()
    
    def stop(self, callback = None):
        self.m_moving = False
        print("Drivar : Stopping the vehicle.")
        if callback is not None:
            callback()
 
    def setDistanceToObstacle(self, distance):
        print("Drivar : Set distance to next obstacle : %d cm", distance)
        self.m_distanceToNextObstacle = distance
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def getDistanceToObstacle(self):
        print("Drivar : Getting distance to obstacle.")
        return self.m_distanceToNextObstacle
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def isObstacleWithin(self, distance):
        print("Drivar : Measuring whether obstacle is within %d cms", distance)
        dist = self.m_distanceToNextObstacle
        if(dist <= distance):
            print("Drivar : Obstacle found within %d cms", distance)
            return True
        else:
            print("Drivar : Obstacle NOT found within %d cms", distance)
            return False
    
    def rotatePen(self, angle):
        print("Drivar : Rotating the pen by %d degrees", angle)

    def getReflectivityMeasurement(self):
        return 150
        #return self.m_lightSensor.get_sample()
        
    def wait(self, milliseconds):
        time.sleep(milliseconds/1000)

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

Drivar.register(DrivarThreejs)

if __name__ == '__main__':
    _drivar = DrivarThreejs()

