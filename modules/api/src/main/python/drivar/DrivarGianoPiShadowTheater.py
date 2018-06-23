#  Driver library for Raspbuggy - GianoPi robot Shadow Theater implementation (camera pan/tilt, spotlight)
'''
Created on Apr 24, 2016

@author: bcopy
'''

from drivar.Drivar import Drivar

import time
import logging
import os

class DrivarGianoPiShadowTheater(DrivarHolonomic, DrivarGianoPiAccessories, SoundVLC):
    def __init__(self):
        SoundVLC.__init__(self,os.getcwd())
    
    
    
    @staticmethod
    def _getDCMotorHatSpeed(speed):
        # override superclass implementation - in the Shadow Theater
        # everything is slow
        return 100
