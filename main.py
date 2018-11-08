# import the necessary packages
from __future__ import print_function
from Application import PhotoBoothApp
from imutils.video import VideoStream
import time

# initialize the video stream and allow the camera sensor to warmup
print("[INFO] warming up camera...")
# use default camera by setting src to 0
vs = VideoStream(src=0).start() 
time.sleep(2.0)

# start the app
pba = PhotoBoothApp(vs)
pba.root.mainloop()

#this might be better
#https://stackoverflow.com/questions/14140495/how-to-capture-a-video-and-audio-in-python-from-a-camera-or-webcam