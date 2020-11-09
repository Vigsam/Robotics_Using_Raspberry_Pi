import RPi.GPIO as gp
import time

gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(17,gp.OUT)

pwm_out1 = gp.PWM(17,50)
pwm_out1.start(0)

while(1):
    pwm_out1.ChangeDutyCycle(0)
    time.sleep(0.5)
    pwm_out1.ChangeDutyCycle(2.5)
    time.sleep(0.5)
    pwm_out1.ChangeDutyCycle(5)
    time.sleep(0.5)
    pwm_out1.ChangeDutyCycle(7.5)
    time.sleep(0.5)
    pwm_out1.ChangeDutyCycle(10)
    time.sleep(0.5)
    
    
    
    