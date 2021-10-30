import pyttsx3


class VoiceOver:
    def __init__(self, voice_id, file, convertor):
        self.convertor = convertor
        self.voice_id = voice_id
        self.file = file

    def voice_ids(self):
        ids = {}
        voices = self.convertor.getProperty('voices')
        i = 1

        for voice in voices:
            ids[i] = voice.id
            i += 1
        return ids

    def speak(self, text):
        self.convertor.setProperty('voice', self.voice_id)
        self.convertor.say(text)
        self.convertor.runAndWait()
        return 0
