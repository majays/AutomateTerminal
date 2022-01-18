import os
import random
from gtts import gTTS
from playsound import playsound



def alexis(audio_string):
    text_to_speech = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 100)
    audio_file = 'voice-' + str(r) + '.mp3'
    text_to_speech.save(audio_file)
    playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
