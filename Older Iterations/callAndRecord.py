#record with callback for playback
import wave
import sys 
import pyaudio
import numpy as np


CHUNK = 4096 #1024 
FORMAT = pyaudio.paInt16 
CHANNELS = 1 if sys.platform == 'darwin' else 2 
RATE = 44100
RECORD_SECONDS = 5 

with wave.open('output.wav', 'wb') as wf: 

    def callback(in_data, frame_count, time_info, status):
        #next line from google AI, unfortunately

        in_data_np = np.frombuffer(in_data, dtype=np.int16)
        #edit audio here
        out_data = in_data_np.tobytes()
        wf.writeframes(out_data) #record to wav
        return(out_data, pyaudio.paContinue)
   
    p = pyaudio.PyAudio() 

    wf.setparams((CHANNELS, p.get_sample_size(FORMAT), RATE, RATE*RECORD_SECONDS, 'NONE', 'not compressed'))

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer= CHUNK, stream_callback=callback) 
    #stream.start_stream()

    input("Press Enter to stop...")
    #stream.stop_stream()
    stream.close() 
    p.terminate() 