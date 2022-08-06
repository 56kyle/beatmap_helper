
from scipy import signal
from scipy.io import wavfile



def load_wav(wav_file):
    sample_rate, samples = wavfile.read('data/original/sub.wav')
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)
    return frequencies, times, spectrogram





