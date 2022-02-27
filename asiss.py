import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    """This Function change our text to audio format"""
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    """This function will speak and wish me
    basis on time of day and ask me for help"""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")  

    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    
    else:
        speak("Good evening")
    speak("i am Jullie Sir. please tell me how can I help you?")


def takeCommand():
    """it takes audio input from user and change it to string"""
    r = sr.Recognizer()
    with sr.Microphone() as source:

        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing... ")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    

    except Exception as e:
        #print(e)
        print("say that again please")
        speak('say that again please')
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        #logic for task on query

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace('wikipedia', '')
            result = wikipedia.summary(query, sentences=2)
            speak('according to wikipedia..')
            print(result)
            speak(result)
        

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        
        elif 'open facebook' in query:
            webbrowser.open('facebook.com')
        
        elif 'open instagram' in query:
            webbrowser.open('instagram.com')
        

        elif 'open google' in query:
            webbrowser.open('google.com')
       

        elif 'open netflix' in query:
            webbrowser.open('netflix.com')
       

        elif 'play music' in query:
            music = 'E:\\memmory\\music'
            songs = os.listdir(music)
            #print(songs)
            os.startfile(os.path.join(music, songs[0]))
        

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H , %M , %S")
            print(strtime)
            speak(strtime)
        
        elif 'quit' in query:
            print('Ok sameer darling. see you later.')
            speak('Ok sameer darling. see you later.')
            exit()
       
# Sameer Ahmed Baloch
#17-Aug_2021          

