import unittest

from drivar.Drivar import Drivar
from drivar.DrivarMqtt import DrivarMqtt
import paho.mqtt.client as mqtt
import time

import logging
import os
from testfixtures import LogCapture

class TestPahoMqttAdapter(unittest.TestCase):
   
    def setUp(self):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect("localhost")
        print("starting MQTT loop")
        self.client.loop_start()
        print("running MQTT loop...")
        
    def tearDown(self):
        print("stopping MQTT client...")
        self.client.disconnect()
        print("MQTT client stopped.")

    def on_message(self, client, userdata, msg):    
        print(msg.topic+" "+str(msg.payload)) 

    def test_move(self):
    #    l = LogCapture(names="drivar.DrivarMqtt",install=False, level=logging.DEBUG)
        drivar = DrivarMqtt(self.client, "/drivar/robot1/in")
        drivar.initialize()
        drivar.motor_move()

    #    l.install()
        time.sleep(1)

        drivar.motor_move(direction=Drivar.DIR_BACKWARD, speed=Drivar.SPEED_FAST, durationInMs=2000)
        
        time.sleep(2)

        drivar.motor_turn(direction=Drivar.DIR_RIGHT, speed=Drivar.SPEED_MEDIUM)
        time.sleep(1)

    #    l.check(('drivar.DrivarMqtt', 'INFO', 'Drivar : Moving all wheels with power '+str(DrivarNoop._getMotorPowerLevel(params['speed']))+'.'),
    #            ('drivar.DrivarMqtt', 'INFO', 'Drivar : Stopping the vehicle.'))
    #    l.clear()
    #    time.sleep(1)
    #    l.check(('drivar.DrivarMqtt','INFO','Drivar : Turning the vehicle left by 90 degrees.'))
    #    l.uninstall()

if __name__ == '__main__':
    unittest.main()
