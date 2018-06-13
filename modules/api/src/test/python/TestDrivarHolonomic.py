import unittest
from drivar.Drivar import Drivar
from drivar.DrivarHolonomic import DrivarHolonomic
import logging
from testfixtures import LogCapture

class TestDrivarHolonomic(unittest.TestCase):
    
    
    def test_move(self):
        l = LogCapture()
        
        drivar = DrivarHolonomic()
        drivar.initialize()
        drivar.motor_move()
#         l.check(('drivar.DrivarHolonomic', 'DEBUG', 'Drivar : initialized'),
#                 ('drivar.DrivarHolonomic', 'INFO', 'Drivar : Moving all wheels with power 70.'),
#                 ('drivar.DrivarHolonomic', 'INFO', 'Drivar : Stopping the vehicle.'))
        drivar.motor_turn()
        
        l.uninstall_all()


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
