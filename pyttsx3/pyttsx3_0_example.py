import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

text = str(input("Paste article\n"))
#speak(text)

engine.save_to_file(text, 'test.mp3')
engine.runAndWait()