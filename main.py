from datetime import *
import wikipedia
import pywhatkit
import pyttsx3

speaker = pyttsx3.init()

try:
    while True:
        command = input('What to do: ')

        if 'date' in command:
            today = date.today()
            print("Current date:", today)
            speaker.say(today)
            speaker.runAndWait()

        elif 'time' in command:
            now = datetime.now()
            current = now.strftime("%H:%M:%S")
            print('time:',current)
            speaker.say(current)
            speaker.runAndWait()
        
        elif 'who' in command:
            person = command.replace('who','')
            sen = "how many paragraphs should I read: "
            para = int(input(sen))
            info = wikipedia.summary(person, para)
            print(info)
            speaker.say(info)
            speaker.runAndWait()

        elif 'play' in command:
            song = command.replace('play', '')
            print('playing....')
            pywhatkit.playonyt(song)

except:
    print('bip bip bip!!')
