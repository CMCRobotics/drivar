import unittest

from drivar.Drivar import Drivar
from drivar.DrivarNoop import DrivarNoop
from drivar.PahoMqttAdapter import PahoMqttAdapter

import logging
import os
from testfixtures import LogCapture

import paho.mqtt.client as mqtt
import json
import time


class TestPahoMqttAdapter(unittest.TestCase):
   
    def setUp(self):
        self.client = mqtt.Client()
        self.client.connect("localhost")
        

    def test_move(self):
        l = LogCapture(names="drivar.DrivarNoop",install=False, level=logging.DEBUG)
        drivar = DrivarNoop()
        drivar.initialize()
        adapter = PahoMqttAdapter(drivar)
        # Test that messages get interpreted correctly
        adapter.start()
        l.install()
        params = {'speed': Drivar.SPEED_FAST}
        self.client.publish("scene/robot/drivar/command/motor/move", json.dumps(params), 0, True)
        time.sleep(1)
        l.check(('drivar.DrivarNoop', 'INFO', 'Drivar : Moving all wheels with power '+str(DrivarNoop._getMotorPowerLevel(params['speed']))+'.'),
                ('drivar.DrivarNoop', 'INFO', 'Drivar : Stopping the vehicle.'))
        l.clear()
        self.client.publish("scene/robot/drivar/command/motor/turn", "", 0, True)
        time.sleep(1)
        l.check(('drivar.DrivarNoop','INFO','Drivar : Turning the vehicle left by 90 degrees.'))
        l.uninstall()

if __name__ == '__main__':
    unittest.main()
