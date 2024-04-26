import speech_recognition as sr 
import pyttsx3
recognizer = sr.Recognizer() 
engine = pyttsx3.init()
def speak(text): 
    engine.say(text) 
    engine.runAndWait()
def listen():
    with sr.Microphone() as source: 
        print("Listening...") 
        recognizer.adjust_for_ambient_noise(source) 
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio) 
        print("User said:", query)
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.") 
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;{0}".format(e))
        return "" 
    def main():
        speak("Hello! I am your Python Voice Assistant. How can I assist you today?") 
        while True:
            query = listen() 
            if "exit" in query:
                speak("Goodbye!") 
                break
            else:

                if 'hello' in query:
                    speak("Hello! How can I help you?") 
                elif "what is your name" in query:
                    speak("I am a Python Voice Assistant.")
 
                elif "how are you" in query:
                    speak("I'm doing well, thank you for asking!") 
                else:
                    speak("Sorry, I didn't understand that command.") 
if  name== " main ":
    main()