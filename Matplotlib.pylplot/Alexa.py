#pip install pyttsx3
#pip install speech recognition
#pip install pywhatkit
#pip install wikipedia
#pip install pyjokes


import Speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia.wikipedia as Wikipedia
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[1].id)


def talk(text):
     engine.say(text)
     engine.runAndWait0

wikipedia.summary(person, 1)
print(info)
talk(info)
     
     
     
def takeCommand():
          try:
               with sr.Microphone() as source:
                    print("Listening...")
                    voice = listener.listen(source)
                    command = listener.recognize_google(voice)
                    command = command.lower()
                    if 'alexa' in command:
                         command
                         command.replace('alexa',"")
                         print(command)
          except:
               pass
          return command
                                                 

def run_alexa():
      command = takeCommand()
      print(command)
      if 'play' in command:
            song = command.replace('play',*)
            talk("playing song")
            pywhatkit.playonyt(song)

     
      elif 'time' in command:
            Time = datetime.datetime.now().strftime("%H:%M:%S")
            talk('Current time is'+ time)

      elif 'who the heck' is in command:
            personcommand = command.replace('who the heck is','')
            info 

      elif 'date' in command:
            talk('sorry, I have a headache')
            
      elif 'Are you single' in command:
            talk("I am relationship with wifi")

      elif 'jokes' in command:
            talk(pyjokes.get_jokes())

      else:
            talk('Sorry,say command again')


          
while True:
     run_alexa()