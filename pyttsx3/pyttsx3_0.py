import pyttsx3

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')   # current speaking rate
print (rate) 
engine.setProperty('rate', 150) 

volume = engine.getProperty('volume')   #current volume level 
print (volume)                          #printing current volume level
engine.setProperty('volume',0.5)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("Hello python")

