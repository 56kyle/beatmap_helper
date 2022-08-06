

import pyaudio
import os
import wave

import numpy as np

CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

class Instrument:
    def __init__(self, data):
        pass




# from http://stackoverflow.com/questions/2226853/interpreting-wav-data/2227174#2227174
def interpret_wav(raw_bytes, n_frames, n_channels, sample_width, interleaved = True):

    if sample_width == 1:
        dtype = np.uint8 # unsigned char
    elif sample_width == 2:
        dtype = np.int16 # signed 2-byte short
    else:
        raise ValueError("Only supports 8 and 16 bit audio formats.")

    channels = np.frombuffer(raw_bytes, dtype=dtype)

    if interleaved:
        # channels are interleaved, i.e. sample N of channel M follows sample N of channel M-1 in raw data
        channels.shape = (n_frames, n_channels)
        channels = channels.T
    else:
        # channels are not interleaved. All samples from channel M occur before all samples from channel M-1
        channels.shape = (n_channels, n_frames)

    return channels


if __name__ == '__main__':
    with open('../data/original/sub.wav', 'rb') as file:
        wav = wave.open(file)
        print(wav)
        p = pyaudio.PyAudio()
        channels = interpret_wav(wav.readframes(wav.getnframes() * wav.getnchannels()), wav.getnframes(), wav.getnchannels(), wav.getsampwidth())
        print(channels)

        '''
        stream = p.open(format=p.get_format_from_width(wav.getsampwidth()),
                        channels=wav.getnchannels(),
                        rate=wav.getframerate(),
                        output=True)
        data = wav.readframes(CHUNK_SIZE)
        frames = [data]
        while data:
            data = wav.readframes(CHUNK_SIZE)
            frames.append(data)
        for channel in channels:
            print(channel)
        print(channels)
        stream.stop_stream()
        stream.close()
        '''
        p.terminate()




