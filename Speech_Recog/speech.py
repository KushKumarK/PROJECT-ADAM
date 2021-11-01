import pyttsx3
from Text_to_speech import VoiceOver as vo
from voice_change import Voice_Change as vc
from speech_rec import speech_to_txt
from user_voice import record_voice as rv

convertor = pyttsx3.init()
voice_id = 1
initial_voice = vo(voice_id, convertor, False)
initial_text = "Hello I am ADAM. Say 'START' to begin"
initial_voice.speak(initial_text)
data = speech_to_txt(initial_voice)
if data["transcript"] in ["Start", "start", "START"]:
    initial_voice.speak("Well Hello...")
    new_data = speech_to_txt(initial_voice)
    dat = "Change to my voice"
    if new_data["transcript"] in [dat, dat.upper(), dat.capitalize(), dat.lower()]:
        initial_voice.speak("I will record your voice for 10 - 20s. Speak some lines for me to interpret")
        user_voice = initial_voice.voice_change("Hello, Now We Are ADAM!")
    new_data = speech_to_txt(initial_voice)
    dat2 = "bye"
    if new_data["transcript"] in [dat, dat.upper(), dat.capitalize(), dat.lower()]:
        initial_voice.speak("Bye!!!")