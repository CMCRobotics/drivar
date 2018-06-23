#  Driver library for Raspbuggy - GianoPi robot accessories implementation (camera pan/tilt, spotlight)
'''
Created on Apr 24, 2016

@author: bcopy
'''

from drivar.Drivar import Drivar

from picamera import PiCamera

import time
import logging

class DrivarGianoPiAccessories(Drivar):
    def spotlight_setIntensity(self, intensity):
        pass
    
    def camera_tiltTo(self, angle):
        pass
    
    def camera_panTo(self, angle):
        pass
    