# AM_MODULATION

# Audio Transmission & Reception Project

This project demonstrates a basic audio transmission workflow using Python. The workflow comprises three main scripts:

1. **cria_audio.py**  
2. **transmissor.py**  
3. **receptor.py**  

Each script handles a different part of the signal flow: **audio creation/recording**, **signal transmission/modulation**, and **signal reception/demodulation**.

---

## Overview

- **`cria_audio.py`**: Records audio from the microphone and saves the raw audio to a file (`audio.wav`).  
- **`transmissor.py`**: Takes the recorded audio, filters and modulates it onto a carrier signal, and saves the modulated signal to `audio_AM.wav`.  
- **`receptor.py`**: Reads the modulated signal, demodulates it, and applies additional filtering to recover the original audio content, saving the final result to `final.wav`.
