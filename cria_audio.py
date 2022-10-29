from typing_extensions import Self
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import sys
import matplotlib.pyplot as plt
from scipy.fftpack import fft
from scipy import signal as window
from scipy.io.wavfile import write
import wavio
import time
def main():
    duration =  5 # #tempo em segundos que ira aquisitar o sinal acustico captado pelo mic
    
    #calcule o numero de amostras "numAmostras" que serao feitas (numero de aquisicoes) durante a gracação. Para esse cálculo você deverá utilizar a taxa de amostragem e o tempo de gravação

    #faca um print na tela dizendo que a captacao comecará em n segundos. e entao 
    #use um time.sleep para a espera
    print("CAPTAÇÃO COMEÇA EM 4 SEGUNDOS")
    #Ao seguir, faca um print informando que a gravacao foi inicializada
    time.sleep(4)
    #para gravar, utilize
    audio = sd.rec(int(duration*44100), 44100,1)
    sd.wait()
    print("...     FIM")
    sd.play(audio)
    sd.wait()
    print(np.size(audio))

    gravado = audio[:,0]

    wavio.write("audio.wav", gravado, 44100, sampwidth=3)
if __name__ == "__main__":
    main()
