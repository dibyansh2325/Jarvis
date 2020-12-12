import speech_recognition as sr 
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

#initialising pyttsx3
engine = pyttsx3.init()
#getting the different accents of voices
voices = engine.getProperty('voices')
#setting the speed of the voice 
engine.setProperty('rate', 160) 
#setting the voice to English US
engine.setProperty('voice', voices[14].id)


#creating a function to talk back whatever is passed in the variable 'text'
def talk(text):
    engine.say(text)
    engine.runAndWait()

#creating a function to recogise voice
def take_command():
    try:
        with sr.Microphone() as source:   #setting microphone as the source of voice
            print("Listening...")
            voice  = listener.listen(source) #storing your voice
            command = listener.recognize_google(voice) #recognising it using google api
            command = command.lower()
            if 'jarvis' in command: #making condition so that it only listens when jarvis is said
                command = command.replace('jarvis', '') #replacing jarvis with blank space so command doesnt have jarvis in it
                print(command)

    except: 
        pass

    return command

#creating final function to run jarvis
def run_jarvis():
    command = take_command()
    print(command) #prints the command given earlier
    #if command has the word play in it, jarvis will play it from youtube
    if 'play' in command: 
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    #if command has time in it, jarvis will tell the time
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current Time is' + time)
    #if command has 'what is' in it, jarvis will return a 1 sentence summery from wikipedia 
    elif 'what is' in command:
        thing = command.replace('what is ', '')
        info = wikipedia.summary(thing, 1)
        print(info)
        talk(info)
    #if command has 'who is' in it, jarvis will return a 1 sentence summery from wikipedia
    elif 'who is' in command:
        person = command.replace('who is ','')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'are you single' in command:
        talk('I am in relationship with internet')

    elif 'joke' in command:
        talk(pyjokes.get_joke())
    #you can always add more conditions according to your wish
    else:
        talk("Sorry I Did not get You")


run_jarvis()