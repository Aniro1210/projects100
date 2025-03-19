import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import psutil

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 125)  # Slow down speech rate

# Set up speech recognition
r = sr.Recognizer()

# Function to speak text
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user
def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good morning, Anirban!")
    elif 12 <= hour < 18:
        speak("Good afternoon, Anirban!")
    else:
        speak("Good evening, Anirban!")

    speak("My name is Jarvis.How can I help you?")       

# Function to process voice commands
def process_command(command):
    command = command.lower()  # Convert to lowercase for better matching

    if "what is your name" in command:
        speak("Hi my name is Jarvis. I'm a virtual assistant.")

    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {current_time}")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "play" in command:
        song = command.replace("play", "").strip()
        if song:
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
        else:
            speak("Please specify a song name.")

    elif "search for" in command:
        query = command.replace("search for", "").strip()
        try:
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia: {results}")
        except wikipedia.exceptions.DisambiguationError:
            speak("There are multiple results. Please specify your search better.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find any results.")

    elif "take a screenshot" in command:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        speak("Screenshot saved.")

    elif "system specs" in command:
        cpu_usage = psutil.cpu_percent()
        memory_usage = psutil.virtual_memory().percent
        speak(f"CPU usage is at {cpu_usage} percent. Memory usage is at {memory_usage} percent.")

    elif "exit" in command or "stop" in command:
        speak("Goodbye! Have a great day.")
        exit()

    else:
        speak("I didn't quite understand that.")

# Function to listen for voice commands
def listen():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)  # Helps with background noise
            audio = r.listen(source)

            command = r.recognize_google(audio, language="en-US")
            print(f"Command: {command}")

            process_command(command)

    except sr.UnknownValueError:
        speak("Could not understand command.")
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
    except OSError as e:
        print(f"Microphone error: {e}")

# Main Execution
if __name__ == "__main__":
    wishMe()  
    while True:
        listen() 