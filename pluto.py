import pyttsx3
import speech_recognition as inp
import wikipedia
import pyautogui
import  webbrowser as br


runner=pyttsx3.init()

def vocal(audio):
    runner.say(audio)
    runner.runAndWait()

def wel():
    vocal('Welcome')
    vocal('This is pluto, how can I help you sir?')

def ss():
    ss=pyautogui.screenshot()
    ss.save("C:\\Users\\Tushar\\Pictures\\Screenshots\\s.png")

def getCmd():
    res=inp.Recognizer()
    with inp.Microphone() as source:
        print('Ready for command')
        res.pause_threshold = 0.5
        audio=res.listen(source)

    try:
        print("Trying to understand")
        query=res.recognize_google(audio,language='en-in')
        print(query)

    except Exception as err:
        vocal('Can you repeat it please sir')

        return "None"
    return query



if __name__ == "__main__":
    wel()
    while True:
        query=getCmd().lower()
        if 'turn off' in query:
            vocal("ok, I am shutting down myself sir")
            quit()
        elif 'wikipedia' in query:
            vocal("ok looking in wikipedia")
            query=query.replace("wikipedia","")
            r=wikipedia.summary(query,sentences=3)
            vocal(r)

        elif 'browse' in query:
            vocal('What I may look for?')
            c='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            srh=getCmd().lower()
            br.get(c).open_new_tab(srh+'.com')

        elif 'take ss' in query:
            ss()
            vocal("taking screenshot")

