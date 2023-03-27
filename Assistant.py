# Welcome Back Script

import pyttsx3 as ps
import time
import requests
import speech_recognition as sr

# Getting Time Information

current_time = time.time()
current_time_tuple = time.localtime(current_time)
current_day = current_time_tuple.tm_wday
weekday_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
current_weekday_name = weekday_names[current_day]
current_year = current_time_tuple.tm_year
current_month = current_time_tuple.tm_mon
current_day_number = current_time_tuple.tm_mday

current_day_format = str(current_year) + "-" + str(current_month) + "-" + str(current_day_number)
print(current_day_format)
# Gather weather forecast information

api_key = "YOUR_API_KEY"

base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = "YOUR_CITY"
complete_url = base_url + "appid=" + 'd850f7f52bf19300a9eb4b0aa6b80f0d' + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]

    current_temperature = y["temp"]
    z = x["weather"]

    weather_description = z[0]["description"]

    temperature = str(round(current_temperature - 273, 1))
    description = str(weather_description)
else:
    temperature = "Could'nt Reach"
    description = "Unreachable"

# Initiating Text to Speech Engine

engine = ps.init()

# Setting up properties

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Things to say

engine.say("Good Morning Sir!")
engine.say("Today is " + current_weekday_name + " " + current_day_format)
# noinspection PyUnboundLocalVariable
engine.say("Weather Report!" + "The temperature seems like " + temperature + "degree celsius, with " + description)
engine.say("Can I Help You?")
engine.runAndWait()

# Initialize Speech Recognition

r = sr.Recognizer()

# Recognizing
print("Recognizing .....")

while 1:

    try:

        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
            Text = r.recognize_google(audio)
            Text = Text.lower()

            print(Text)
            engine.say(Text)
            engine.runAndWait()

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:

        print("Unknown Error Occurred")

# noinspection PyUnreachableCode
print("Completed!")