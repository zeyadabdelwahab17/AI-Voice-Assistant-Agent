import pyttsx3

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)   # 150 words/minute
    engine.say(text)
    engine.runAndWait()