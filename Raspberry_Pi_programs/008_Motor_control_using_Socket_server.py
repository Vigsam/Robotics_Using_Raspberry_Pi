import socket
import RPi.GPIO as gp
import time
from picamera import PiCamera

gp.setwarnings(False)
gp.setmode(gp.BCM)

s = socket.socket()
camera = PiCamera()
s.bind(('0.0.0.0',8081))  #Tuple,Accept all the client from Ip address(0-255.0-255.0-255.0-255)

s.listen(1) #Listening to a client

#we have to connect these PWM pins to Enable pins such as A, B of L298N driver respectively

gp.setup(12,gp.OUT)  # PWM Pin Motor1
gp.setup(19,gp.OUT)  # PWM Pin Motor2

#we have to connect 16,20 digital pins to the Input pins 1 and 2
#we have to connect 21,26 digital pins to the Input pins 3 and 4

gp.setup(16,gp.OUT)
gp.setup(20,gp.OUT)
gp.setup(21,gp.OUT)
gp.setup(26,gp.OUT)

pwm_out1 = gp.PWM(12,100)
pwm_out2 = gp.PWM(19,100)

pwm_out1.start(0)
pwm_out2.start(0)

gp.output(16,0)
gp.output(20,0)
gp.output(21,0)
gp.output(26,0)

while(1):
    client, addr = s.accept()
    
    while(1):
        content = client.recv(10)
        if(len(content)==0):
            break
        else:
            print(content)
            if(content == b'f\r\n'):
                client.send(bytes('Forward\r\n','utf-8'))
                pwm_out1.ChangeDutyCycle(15)
                pwm_out2.ChangeDutyCycle(15)
                gp.output(16,1)
                gp.output(20,0)
                gp.output(21,1)
                gp.output(26,0)
                
            elif(content == b'b\r\n'):
                client.send(bytes('Backward\r\n','utf-8'))
                pwm_out1.ChangeDutyCycle(15)
                pwm_out2.ChangeDutyCycle(15)
                gp.output(16,0)
                gp.output(20,1)
                gp.output(21,0)
                gp.output(26,1)
            
            elif(content == b'r\r\n'):
                client.send(bytes('Right\r\n','utf-8'))
                pwm_out1.ChangeDutyCycle(15)
                pwm_out2.ChangeDutyCycle(15)
                gp.output(16,1)
                gp.output(20,0)
                gp.output(21,0)
                gp.output(26,0)
                
            elif(content == b'l\r\n'):
                client.send(bytes('Left\r\n','utf-8'))
                pwm_out1.ChangeDutyCycle(15)
                pwm_out2.ChangeDutyCycle(15)
                gp.output(16,0)
                gp.output(20,0)
                gp.output(21,1)
                gp.output(26,0)
            
            elif(content == b's\r\n'):
                client.send(bytes('Stop\r\n','utf-8'))
                pwm_out1.ChangeDutyCycle(15)
                pwm_out2.ChangeDutyCycle(15)
                gp.output(16,0)
                gp.output(20,0)
                gp.output(21,0)
                gp.output(26,0)
                
            elif(content == b'start\r\n'):
                client.send(bytes('Recording Started\r\n','utf-8'))
                camera.start_recording('/home/pi/Desktop/video1.h264')
            
            elif(content == b'stop\r\n'):
                client.send(bytes('Recording Stopped\r\n','utf-8'))
                camera.stop_recording()
                
                 
    print("Closing Connection")
    client.close()    
