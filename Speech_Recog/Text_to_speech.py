from user_voice import record_voice 
from voice_change import Voice_Change
import sounddevice as sd

class VoiceOver:
    def __init__(self, voice_id, convertor, usr_voice = False):
        self.usr_voice = usr_voice
        self.convertor = convertor
        self.voice_id = voice_id

    def voice_ids(self):
        ids = {}
        voices = self.convertor.getProperty('voices')
        i = 1

        for voice in voices:
            ids[i] = voice.id
            i += 1
        return ids

    def speak(self, text):
        if not self.usr_voice:
            ids_voice = self.voice_ids()
            self.convertor.setProperty('voice', ids_voice[self.voice_id])
            self.convertor.say(text)
            self.convertor.runAndWait()
            return 0
        elif self.usr_voice:
            voice = self.voice_change(text)
            sd.play(voice[0], voice[1])
            sd.wait()
            return 0

    def voice_change(self, text):
        path = record_voice()
        user = Voice_Change(path)
        self.usr_voice = True
        generated_voice = user.voice_speak(text)
        return generated_voice


