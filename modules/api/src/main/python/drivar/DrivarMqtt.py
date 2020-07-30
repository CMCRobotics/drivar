#  Driver library for a Browser-based MQTT client
'''
Created on Aug 01, 2020

@author: bcopy
'''

from drivar.Drivar import Drivar
import time
import logging

logging.basicConfig()

class DrivarMqtt(Drivar):
    """
     Translates Drivar calls into MQTT messages
    """
    def __init__(self, mqttClient, topic):
        self.initialized = False
        self.moving = False
        self.logger = logging.getLogger(__name__)
        self.distanceToNextObstacle = 2000
        self.mqttClient = mqttClient
        self.topic = topic

    def initialize(self):
        super(DrivarMqtt,self).initialize()
        self.logger.debug("Drivar MQTT : initialized")
        self.initialized = True
        

    def motor_move(self, direction=Drivar.DIR_FORWARD,durationInMs=1000, speed = Drivar.SPEED_SLOW, callback = None):
        durationInMs = max(durationInMs,100)
        _direct = direction
        _speed = speed
        self.motor_rotateWheels(direction = _direct, speed = _speed)
        self.time_wait(durationInMs/1000)
        self.motor_stop()
        if callback is not None:
            callback()
    
    def motor_rotateWheels(self, wheelSet = Drivar.WHEELS_BOTH, direction = Drivar.DIR_FORWARD, speed = Drivar.SPEED_SLOW, callback = None):
        _power = self._getMotorPowerLevel(speed)
        _steer = 0
        # Correct the power (positive vs negative) depending on the direction
        if(direction == Drivar.DIR_FORWARD):
            if(_power < 0):
                _power = _power * -1
        if(direction == Drivar.DIR_BACKWARD):
            if(_power > 0):
                _power = _power * -1
        # Get the wheels turning
        _wheelSet = 'all'
        if(wheelSet == Drivar.WHEELS_LEFT):
            _wheelSet = 'left'
            _steer = 900
        if(wheelSet == Drivar.WHEELS_RIGHT):
            _wheelSet = 'right'
            _steer = -900
        
        self.logger.info("Drivar : Moving %s wheels with power %d.", _wheelSet,_power)
        self.mqttClient.publish(self.topic,'move steer={},speed={}'.format(_steer,_power))
        self.moving = True
        if callback is not None:
            callback()
        
    def motor_turn(self, direction = Drivar.DIR_LEFT, angle = 90,  speed = Drivar.SPEED_SLOW, callback = None):
        _dir = "left"
        _wheelSet = Drivar.WHEELS_LEFT
        if(direction == Drivar.DIR_RIGHT):
            _dir = "right"
            _wheelSet = Drivar.WHEELS_RIGHT
        self.logger.info("Drivar : Turning %s ", _dir)
        
        self.motor_rotateWheels(wheelSet = _wheelSet, speed = speed)
        self.time_wait(200/1000)
        self.motor_stop()
        if callback is not None:
            callback()
    
    def motor_stop(self, callback = None):
        self.moving = False
        self.logger.info("Drivar : Stopping the vehicle.")
        self.mqttClient.publish(self.topic,'move steer={},speed={}'.format(0,0))
        if callback is not None:
            callback()
 
    def time_wait(self, durationInMs = 1000):
        self.logger.info("Drivar : Sleeping for %s milliseconds.", durationInMs)
        time.sleep(durationInMs/1000)

    '''
      Return the MQTT speed equivalent for the given DRIVAR speed flag
    '''
    @staticmethod
    def _getMotorPowerLevel(speed):
        if(speed==Drivar.SPEED_SLOW):
            return 300
        elif(speed==Drivar.SPEED_MEDIUM):
            return 700
        elif(speed==Drivar.SPEED_FAST):
            return 1024
        else :
            return 300 

Drivar.register(DrivarMqtt)

if __name__ == '__main__':
    _drivar = DrivarMqtt()
