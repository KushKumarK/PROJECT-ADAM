from user_voice import record_voice 
from voice_change import Voice_Change
import sounddevice as sd

class VoiceOver:
    def __init__(self, voice_id, convertor, usr_voice = False):
        self.usr_voice = usr_voice
        self.convertor = convertor
        self.voice_id = voice_id
        self.voice = []

    def voice_ids(self):
        ids = {}
        voices = self.convertor.getProperty('voices')
        i = 1

        for voice in voices:
            ids[i] = voice.id
            i += 1
        return ids

    def speak(self, text = "", voice = []):
        if not self.usr_voice:
            ids_voice = self.voice_ids()
            self.convertor.setProperty('voice', ids_voice[self.voice_id])
            self.convertor.say(text)
            self.convertor.runAndWait()
            return 0
        elif self.usr_voice:
            sd.play(voice[0], voice[1])
            sd.wait()
            return 0

    def voice_change(self, text, path):
        user = Voice_Change(path)
        self.usr_voice = True
        self.voice = user.voice_speak(text)
        return self.voice


