from drivar.Drivar import Drivar
from drivar.DrivarHolonomic import DrivarHolonomic
drivar = DrivarHolonomic()
drivar.initialize()
drivar.motor_move(durationInMs= 5000)