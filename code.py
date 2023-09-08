
# These lines import the necessary libraries to run this code
import time
import board
import digitalio
import pwmio

from adafruit_motor import motor #Imports a function from the adfruit_motor libary

right_motor_forward = board.GP14 #Initializes the varible right_motor_forward and it attaches it to GP12
right_motor_backward = board.GP15 #Initializes the varible right_motor_backward and it attaches it to GP13
left_motor_forward = board.GP12
left_motor_backward = board.GP13

pwm_Ra = pwmio.PWMOut(right_motor_forward, frequency=10000) #It tells controller tthat the motor is an output
pwm_Rb = pwmio.PWMOut(right_motor_backward , frequency=10000)  #It tells controller tthat the motor is an output
pwm_La = pwmio.PWMOut(left_motor_forward, frequency=10000)
pwm_Lb = pwmio.PWMOut(left_motor_backward , frequency=10000)

Left_Motor = motor.DCMotor(pwm_La, pwm_Lb) # Configuration line(it is required)
Left_Motor_speed = 0 # Initantes the varible for the left_motor_speed and it starts it at 0
right_Motor = motor.DCMotor( pwm_Ra, pwm_Rb)
right_Motor_speed = 0




while True:

    Left_Motor_speed = -1  #Left motor backwards
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    Left_Motor_speed = 1
    Left_Motor.throttle = Left_Motor_speed
    time.sleep(2)
    right_Motor_speed = -1
    right_Motor.throttle = right_Motor_speed
    time.sleep(10)
    right_Motor_speed = 1
    right_Motor.throttle = right_Motor_speed
    time.sleep(2)


