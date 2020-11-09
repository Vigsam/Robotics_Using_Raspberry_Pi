import RPi.GPIO as gp
import time

gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(12,gp.OUT)

pwm_out1 = gp.PWM(12,100)
pwm_out1.start(0)

while(1):
    for duty in range(0,101,1):
        pwm_out1.ChangeDutyCycle(duty)
        time.sleep(0.01)
    for duty in range(100,-1,-1):
        pwm_out1.ChangeDutyCycle(duty)
        time.sleep(0.01)    
    

