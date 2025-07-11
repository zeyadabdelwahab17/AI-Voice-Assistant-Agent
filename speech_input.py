import sounddevice as sd
import queue
import vosk
import json

q = queue.Queue()
model = vosk.Model(r"C:\Users\Lenovo\Downloads\my_sight_voice\vosk-model-small-en-us-0.15")

def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))

def recognize_speech():
    with sd.RawInputStream(samplerate=16000, blocksize=8000, dtype="int16",
                           channels=1, callback=callback):
        rec = vosk.KaldiRecognizer(model, 16000)
        print("Listening...")

        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                return result.get("text", "")