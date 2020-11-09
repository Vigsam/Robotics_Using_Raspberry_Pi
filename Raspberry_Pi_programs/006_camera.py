from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
time.sleep(4)
camera.capture('/home/pi/Desktop/image_1.jpg')
camera.stop_preview()

camera.start_preview()
camera.start_recording('/home/pi/Desktop/video_1.h264')
time.sleep(10)
camera.stop_recording()
camera.stop_preview()