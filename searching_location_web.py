from playsound import playsound
import speech_recognition as sr
import webbrowser
import speak as sp


r = sr.Recognizer()
def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        voice_data = ''

        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            sp.alexis('Sorry, I did not get that')
        except sr.RequestError:
            sp.alexis('Sorry, my service is down')
        return voice_data


def search_():
    sp.alexis('what do you want to search for')
    search = record_audio()
    url = 'https://google.com/search?q=' + search
    webbrowser.get().open(url)
    sp.alexis('Here is what I found for you' + search)


def find_location():
    sp.alexis('Which location do you want to search')
    location = record_audio()
    url = 'https://google.nl/maps/place/' + location + '/&amp'
    webbrowser.get().open(url)
    sp.alexis('Here is what I found fou ' + location)
