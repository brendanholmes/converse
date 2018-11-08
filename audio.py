import pyaudio
import time

class AudioStream:
    def __init__(self, videoStream):
        self.WIDTH = 2
        self.CHANNELS = 2
        self.RATE = 44100
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=self.p.get_format_from_width(self.WIDTH),
                    channels=self.CHANNELS,
                    rate=self.RATE,
                    input=True,
                    output=True,
                    stream_callback=self.callback)
    
        self.stream.start_stream()
    
        while self.stream.is_active():
            time.sleep(0.1)
        
    def callback(self, in_data, frame_count, time_info, status):
        return (in_data, pyaudio.paContinue)        
    
    def StopStream(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()