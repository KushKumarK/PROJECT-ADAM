import speech_recognition as sr
import pyaudio as pa

r = sr.Recognizer()
mic = sr.Microphone()


def speech_to_txt(rec, mic):
    data = {"transcript": "", "success": True}
    recieved = False
    r.dynamic_energy_threshold = True
    try:
        with mic as source:
            print("Calibarating.......")
            r.adjust_for_ambient_noise(source, duration=5)
            print("Speak now...")
            audio = rec.listen(source)
        speech2txt = r.recognize_google(audio)
        data["transcript"] = speech2txt
    except sr.UnknownValueError:
        data["success"] = False

    return data

while True:
        rec = speech_to_txt(r, mic)
        if rec["success"]:
            print(f"The text spoken is: {rec['transcript']}")
            print("Do you want to exit..... Say yes or no")
            ans = speech_to_txt(r, mic)
            if ans["transcript"] in ["yes", "Yes"]:
                print("Well you are exiting....")
            break
        elif not rec["success"]:
            continue
        continue