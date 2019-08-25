import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))

        engine = pyttsx3.init()

        engine.say(format(text))
        engine.runAndWait()

    except:
        print("Sorry could not recognize what you said")