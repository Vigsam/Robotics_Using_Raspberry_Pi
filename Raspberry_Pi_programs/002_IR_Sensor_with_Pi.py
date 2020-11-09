import time

import RPi.GPIO as gp

gp.setwarnings(False)
gp.setmode(gp.BCM)

gp.setup(14, gp.IN)

while(1):
    sensor_data = gp.input(14)
    print(sensor_data)
    time.sleep(2)
