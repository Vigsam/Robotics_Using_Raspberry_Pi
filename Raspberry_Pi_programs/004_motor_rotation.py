import RPi.GPIO as gp
import time
gp.setwarnings(False)
gp.setmode(gp.BCM)

#we have to connect these PWM pins to Enable pins such as A, B of L298N driver respectively

gp.setup(12,gp.OUT)  # PWM Pin Motor1
gp.setup(19,gp.OUT)  # PWM Pin Motor2

#we have to connect 16,20 digital pins to the Input pins 1 and 2.
#we have to connect 21,26 digital pins to the Input pins 3 and 4.

#The combination of these two pins decide direction of the motor

gp.setup(16,gp.OUT)
gp.setup(20,gp.OUT)
gp.setup(21,gp.OUT)
gp.setup(26,gp.OUT)

pwm_out1 = gp.PWM(12,100)
pwm_out2 = gp.PWM(19,100)

pwm_out1.start(0)
pwm_out2.start(0)


while(True):
    pwm_out1.ChangeDutyCycle(100)
    pwm_out2.ChangeDutyCycle(100)
    
    # Forward Rotation of Motor
    
    gp.output(16,1)  #Motor 1
    gp.output(20,0)  #Motor 1
    
    gp.output(21,1)  #Motor 2
    gp.output(26,0)  #Motor 2
    time.sleep(5)
    
    # Reverse Rotation of motor
    
    pwm_out1.ChangeDutyCycle(100)
    pwm_out2.ChangeDutyCycle(100)
    
    gp.output(16,0)  #Motor 1
    gp.output(20,1)  #Motor 1
    
    gp.output(21,0)  #Motor 2
    gp.output(26,1)  #Motor 2
    time.sleep(5)
    
    gp.output(16,0)  #Motor 1
    gp.output(20,0)  #Motor 1
    
    gp.output(21,0)  #Motor 2
    gp.output(26,0)  #Motor 2
    
    time.sleep(5)
    