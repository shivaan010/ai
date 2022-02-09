from datetime import *
import wikipedia
import pywhatkit
import pyttsx3
import smtplib

speaker = pyttsx3.init()

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('ishaans142@gmail.com','programming')

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

        elif 'table' in command:
            table = int(input('Which table too tell: '))
            i = 1
            while i <= 10:
                b = table, 'times', i, '=', table*i
                speaker.say(b)
                speaker.runAndWait()
                i = i+1

        elif 'email' in command:
            sendto = input('who to send email: ')
            text = input('Enter text: ')

            server.sendmail('ishaans@gmail', sendto, text)
            print('send successfully!')

except:
    print('bip bip bip!!')