import speech_recognition as sr
import terminalfun as pr3
import deep as sng
from playsound import playsound
import speak as sp
import searching_location_web as fe

r=sr.Recognizer() 
while True:
    with sr.Microphone() as source:
        sp.alexis("which service do you want to use?")
        print("""please tell me which fuction you will use 
        1) terminal
        2) play music
        3) search web
        4) find location 
        """)
        
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print('you said : {}'.format(text))
            sp.alexis(text)
            
            if text=='quit':
                break
            
            elif text.lower() == 'terminal':  
                pr3.terminal()
            
            elif text.lower() == 'play music':
                sng.playSong()
            
            elif text.lower() == 'search web':
                fe.search_()
            
            elif text.lower() == 'find location':
                fe.find_location()
                
        except:
            print("exception has been occer")
