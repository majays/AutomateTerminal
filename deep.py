import speech_recognition as sr
import amprime as hy
import speak as sp

r=sr.Recognizer()
def playSong():
    with sr.Microphone() as source:
        sp.alexis("speek a song name which you most like ")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        sp.alexis(text)
        song=text.replace('hello deep','')
        hy.playonyt(song)
