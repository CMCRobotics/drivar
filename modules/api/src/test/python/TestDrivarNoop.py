import unittest
from drivar.Drivar import Drivar
from drivar.DrivarNoop import DrivarNoop
import logging
from testfixtures import LogCapture

class TestDrivarNoop(unittest.TestCase):
    
    
    def test_move(self):
        l = LogCapture()
        
        drivar = DrivarNoop()
        drivar.initialize()
        drivar.motor_move()
        l.check(('drivar.DrivarNoop', 'DEBUG', 'Drivar : initialized'),
                ('drivar.DrivarNoop', 'INFO', 'Drivar : Moving all wheels with power 70.'),
                ('drivar.DrivarNoop', 'INFO', 'Drivar : Stopping the vehicle.'))
        drivar.motor_turn()
        
        l.uninstall_all()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
