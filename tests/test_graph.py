
import pytest

import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile


def test_graph():
    sample_rate, samples = wavfile.read('data/original/sub.wav')
    frequencies, times, spectrogram = signal.spectrogram(samples, sample_rate)

    plt.pcolormesh(times, frequencies, spectrogram)
    plt.imshow(spectrogram)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()


def test_other_graph():
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True
    input_data = wavfile.read('data/original/sub.wav')
    audio = input_data[1]
    plt.plot(audio)
    plt.ylabel("Amplitude")
    plt.xlabel("Time")
    plt.show()


