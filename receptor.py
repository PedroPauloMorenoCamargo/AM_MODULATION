from typing_extensions import Self
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
from scipy import signal as window
from scipy.io.wavfile import write
import wavio
import time
from scipy.io import wavfile
import math
from scipy.signal import butter, lfilter, freqz,filtfilt
from scipy import signal as sg
from scipy.signal import kaiserord, lfilter, firwin, freqz

def calcFFT(signal, fs):
    # https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
    N  = len(signal)
    W = window.hamming(N)
    T  = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal*W)
    return(xf, np.abs(yf[0:N//2]))
def butter_highpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = sg.butter(order, normal_cutoff, btype='high', analog=False)
    return b, a

def butter_highpass_filter(data, cutoff, fs, order=5):
    b, a = butter_highpass(cutoff, fs, order=order)
    y = sg.filtfilt(b, a, data)
    return y
def main():
    samplerate, data = wavfile.read('audio_AM.wav')
    tempo = len(data)/samplerate
    t = np.linspace(0,int(tempo),int(tempo)*samplerate)
    sd.play(data,samplerate)
    sd.wait()
    x,y = calcFFT(data,samplerate)
    plt.plot(x, np.abs(y))
    plt.title('Fourier')
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Im (G)")
    plt.show()
    fp = 14000
    Portadora =  np.sin(2*np.pi*fp*t)
    demodulado = data*Portadora
    x,y = calcFFT(demodulado,samplerate)
    plt.plot(x, np.abs(y))
    plt.title('Fourier')
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Im (G)")
    plt.show()

    # The Nyquist rate of the signa
    nyq_rate = samplerate / 2.0

    # The desired width of the transition from pass to stop,
    # relative to the Nyquist rate.  We'll design the filter
    # with a 5 Hz transition width.
    width = 5.0/nyq_rate

    # The desired attenuation in the stop band, in dB.
    ripple_db = 60.0

    # Compute the order and Kaiser parameter for the FIR filter.
    N, beta = kaiserord(ripple_db, width)

    # The cutoff frequency of the filter.
    #cutoff_hz = 2198.0
    cutoff_hz = 2200.0

    # Use firwin with a Kaiser window to create a lowpass FIR filter.
    taps = firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

    # Use lfilter to filter x with the FIR filter.
    filtrado = lfilter(taps, 1.0, demodulado)
    x,y = calcFFT(filtrado,samplerate)
    plt.plot(x, np.abs(y))
    plt.title('Fourier')
    plt.xlabel("Frequência (Hz)")
    plt.ylabel("Im (G)")
    plt.show()
    wavio.write("final.wav", filtrado, 44100, sampwidth=3)

if __name__ == "__main__":
    main()