import speech_recognition as sr
import pyaudio as pa
from Text_to_speech import VoiceOver as vc



def speech_to_txt(voice):
    r = sr.Recognizer()
    mic = sr.Microphone()
    data = {"transcript": "", "success": True}
    r.dynamic_energy_threshold = True
    try:
        with mic as source:
            voice.speak("Calibrating....")
            r.adjust_for_ambient_noise(source, duration=5)
            voice.speak("Speak now...")
            audio = r.listen(source)
        speech2txt = r.recognize_google(audio)
        data["transcript"] = speech2txt
    except sr.UnknownValueError:
        data["success"] = False
    return data


