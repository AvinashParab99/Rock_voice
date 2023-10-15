import speech_recognition as sr
import os
import pyttsx3
import time
from datetime import date
import webbrowser
import geocoder
import datetime
import wikipedia
import pyautogui



# Initialize the recognizer and engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

#voice male female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

"""All function for task"""

#1. For current time
def time_in():
    curr_time = time.strftime("%H:%M:%S", time.localtime())
    speak(f'its {curr_time} right now')


#2. Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()


#3 for current date
def date_in():
    today = date.today()
    speak(f'today date is {today}')


#4.Using the geocoder library to get current location
def location():
        location = geocoder.ip('me')
        city = location.city
        speak(f'your current location is {city}')


#5.for open any application in system
def program_on():
    app_name = user_input.split("open ")[1]
    try:
        os.system(f"start {app_name}.exe")  # This will open the application
        speak(f"Opening {app_name}")
    except Exception as e:
        print(e)
        speak(f"Sorry, I could not open {app_name}")


#6.Function to take user's voice input
def get_audio():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-IN')
            print(f"User said: {query}")
            return query
        except Exception as e:
            print(e)
            return "Sorry, could not understand your voice."


#7 for any calculation
def calculate_expression(expression):
    try:
        result = eval(expression)
        return result
    except Exception as e:
        print(e)
        return "Sorry, I could not perform the calculation."

#8 welcome

def welcome():
    x = datetime.datetime.now().hour
    if x > 12 and x < 17:
        speak("Hey Good Afternoon")
    elif x > 17 and x < 20:
        speak("Hey Good evening")
    elif x > 20 and x < 5:
        speak("Hey Good night")
    else:
        speak("Hey Good morning")


#9 wickipedia
def information(user_input):
    if 'wikipedia' in user_input:
        user_input = user_input.replace('wikipedia', '')
        result1 = wikipedia.summary(user_input, sentences=3)
        print(result1)
        speak(result1)
    elif 'who is' in user_input:
        user_input = user_input.replace('who is', '')
        result1 = wikipedia.summary(user_input, sentences=3)
        print(result1)
        speak(result1)
    elif 'information' in user_input:
        user_input = user_input.replace('information', '')
        result1 = wikipedia.summary(user_input, sentences=3)
        print(result1)
        speak(result1)

# screenshot
def screenshot():
    # Take a screenshot of the entire screen
    screenshot = pyautogui.screenshot()

    # Save the screenshot to a file
    screenshot.save('screenshot.png')

    print('Screenshot captured and saved as screenshot.png')
    speak('Screenshot captured and saved succsessfully')

# Main function
if __name__ == "__main__":
    welcome()
    speak("my name is rock what is your name?")

    user_name = get_audio()
    if "my name is" in user_name:
        uzern=user_name[10::]
        speak(f"oh welcome , {uzern}, Hope you doing well")
    else:
        uzern=user_name
        speak(f"oh welcome , {uzern}, Hope you doing well")
    speak(f'now tell how can i help you {uzern}')

    while True:

        user_input = get_audio().lower()

        if "bye" in user_input:
            speak(f"Goodbye {uzern}!Have a great day! see you soon")
            break

        elif any(keyword in user_input for keyword in ["wikipedia", "who is", "information"]):
            information(user_input)


        elif "time" in user_input:
            time_in()

        elif "screenshot" in user_input:
            screenshot()

        elif "calculate" in user_input:
            # Extract the mathematical expression from the command
            if 'x' in user_input:

                user_input = user_input.replace('x', '*')
                expression = user_input.split("calculate ")[1]
                result = calculate_expression(expression)
                speak(f"The result is {result}")
            else:

                expression = user_input.split("calculate ")[1]
                result = calculate_expression(expression)
                speak(f"The result is {result}")

        elif "search" in user_input:
            # Extract the search query from the command
            query = user_input.replace("search", "")
            url = "https://www.google.com"
            url1 = url.replace("google", query[1::])
            speak(f'searching {query}')
            webbrowser.open(url1)

        elif "thank" in user_input:
            speak(f'oh bye {uzern} have a nice day')
            break

        elif "date" in user_input:
            date_in()

        elif any(keyword in user_input for keyword in ["location", "city", "where i am"]):
            location()

        elif "open" in user_input:
            program_on()

        elif "stop" in user_input:
            speak(f'thank you see you soon {uzern}')
            break
        else:

            speak("Sorry, I didn't understand that.")
