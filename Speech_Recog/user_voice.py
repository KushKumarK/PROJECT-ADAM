from voice_change import Voice_Change as vc
import sounddevice as sd
from scipy.io.wavfile import write

def record_voice():
    fs = 44100
    seconds = 10
    print("Recording........")
    print("Please speak for 10 seconds after the beep")
    myrec = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    sd.wait()
    path = 'Speech_Recog/Resources/user_voice.wav' 
    write(path, fs, myrec)
    return path


