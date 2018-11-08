# import the necessary packages
from __future__ import print_function
from user_interface import UserInterface
from imutils.video import VideoStream
#import time
from audio import AudioStream

# initialize the video stream (use default camera by setting src to 0)
videoStream = VideoStream(src=0).start()
#time.sleep(2.0)
audioStream = AudioStream()

# start the app
pba = UserInterface(videoStream, audioStream)
pba.root.mainloop()

#this might be better
#https://stackoverflow.com/questions/14140495/how-to-capture-a-video-and-audio-in-python-from-a-camera-or-webcam

"""
SOURCE ELEMENTS:

Audio Source Microphone block captures real-world audio samples at a  sampling rate Fs
Amplitude Control: Use this to reduce the dynamic range of the audio signal.
Uniform Encoder: Uniformly quantize and encode the input into specified number of bits (nbits). The input is saturated at positive and negative Peak value. Output datatype is either 8, 16, or 32-bit signed or unsigned integer, based on the least number of bits needed.
Apply Fixed delay: Models the propagation delay in the network
Apply Random Delay: Models the effect of jittering in the network.
UDP send: Transmit audio packets over the IP network with user data gram protocol (UDP)

DESTINATION ELEMENTS: 
         7. Receive UDP packets from the the other PC and fill up the Buffer.
         8.  Uniform decoder:Uniformly decode the input with positive and negative      
         9. Speaker and Time scope for analysis

"""