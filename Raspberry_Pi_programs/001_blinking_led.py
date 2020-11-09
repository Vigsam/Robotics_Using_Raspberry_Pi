import time

import RPi.GPIO as gp

gp.setwarnings(False)
gp.setmode(gp.BCM)
gp.setup(18,gp.OUT)

while(True):
    gp.output(18,1)
    time.sleep(1)
    gp.output(18,0)
    time.sleep(1)