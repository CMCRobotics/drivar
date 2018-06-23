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

    def motor_move(self, direction = DIR_FORWARD,durationInMs=1000, speed = SPEED_SLOW, callback = None):
        pass
    
    def motor_rotateWheels(self, wheelSet = WHEELS_BOTH, direction = DIR_FORWARD, speed = SPEED_SLOW, callback = None):
        pass
    
    def motor_turn(self, direction = DIR_LEFT, angle = 90, callback = None):
        pass

    def motor_stop(self, callback = None):
        pass
 
    '''
      Return the distance to the nearest obstacle, in centimeters
    '''
    def range_getDistanceToObstacle(self):
        pass
 
    '''
      Indicate with a boolean whether there is an obstacle within the given distance
    '''
    def range_isObstacleWithin(self, distance):
        return False
        
    def time_wait(self, duration = 1000):
        time.sleep(duration/1000)
        
    '''
      Orders the pen to be raised or lowered
    '''
    def pen_rotate(self, angle):
        pass

    def reflectivity_get(self):
        return 0

    def sound_playAsync(self, sound):
        pass
    
    def sound_stop(self):
        pass
    
    def sound_setVolume(self, level):
        pass
    
    def spotlight_setIntensity(self, intensity):
        pass
    
    def spotlight_thunder(self, duration=0):
        # Start a thread that simulates thunder and random lightnings
        pass
    
    def spotlight_wave(self, duration=0):
        # Start a thread that simulates a breathing (sin wave)
        pass

    def camera_tiltTo(self, angle):
        pass
    
    def camera_panTo(self, angle):
        pass
    
    def camera_setCapture(self, active):
        pass
    
    def camera_isCapturing(self):
        return False

