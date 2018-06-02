#  Driver library for Raspbuggy
'''
Created on Mar 18, 2015

@author: bcopy
'''
from abc import ABCMeta,abstractmethod
import time



class Drivar(metaclass=ABCMeta):
#class Drivar():
#    __metaclass__ = ABCMeta
    
    DIR_FORWARD = 0x01
    DIR_BACKWARD = 0x02
    
    DIR_LEFT = 0x01
    DIR_RIGHT = 0x02
    
    DIR_PORTSIDE = 0x03
    DIR_STARBOARD = 0x04

    WHEELS_RIGHT = 0x01
    WHEELS_LEFT = 0x02
    WHEELS_BOTH = 0x03
    
    SPEED_SLOW = 0x01
    SPEED_MEDIUM = 0x02
    SPEED_FAST = 0x03
    
    PEN_RAISE = 0x01
    PEN_LOWER = 0x02
    
    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def motor_move(self, direction = DIR_FORWARD,durationInMs=1000, speed = SPEED_SLOW, callback = None):
        pass
    
    @abstractmethod
    def motor_rotateWheels(self, wheelSet = WHEELS_BOTH, direction = DIR_FORWARD, speed = SPEED_SLOW, callback = None):
        pass
    
    @abstractmethod
    def motor_turn(self, direction = DIR_LEFT, angle = 90, callback = None):
        pass

    @abstractmethod
    def motor_stop(self, callback = None):
        pass
 
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    @abstractmethod
    def range_getDistanceToObstacle(self):
        pass
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    @abstractmethod
    def range_isObstacleWithin(self, distance):
        pass
        
    def time_wait(self, duration = 1000):
        time.sleep(duration/1000)
        
    '''
      Orders the pen to be raised or lowered
    '''
    @abstractmethod
    def pen_rotate(self, angle):
        pass

    @abstractmethod
    def reflectivity_get(self):
        pass


