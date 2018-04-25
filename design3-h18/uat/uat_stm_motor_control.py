from atlas.context.runtime_contexts import RealStmRealVisionContext
from atlas.motor.motor_control import MotorControl

context = RealStmRealVisionContext()
motor_control = context.serviceLocator.get(MotorControl)

motor_control.move_forward(0.05)
print("hello")
