# Imports
import datetime
from weather import get_weather
from chat import *
from schedule import *
import pyttsx3
import time
engine = pyttsx3.init()

# Command matches
time_cmd = [
    "what time is it",
    "what is the time",
    "what's the time"
]

date = [
    "what's the date",
    "what is the date",
    "today's date",
    "what date is today"
]

weather_commands = [
    "what's the weather like",
    "how is the weather",
    "what's the temperature",
    "what's the forecast",
    "what's the weather forecast",
    "how's the weather",
    "is it going to rain",
    "do I need an umbrella",
    "should I wear a coat",
    "what should I wear today"
]

my_name_qus = [
    "what's your name",
    "what is your name",
    "what may I call you",
    "tell me about yourself",
    "tell me about you",
    "are you single",
    "How do you look like",
]

routine_cmd = [
    "tomorrow's class",
    "tomorrow's routine",
    "tomorrow's schedule",
    "class i have tomorrow",
    "classes i have tomorrow",
]


imgGen = [
    "imagine",
    "draw",
    "paint",
    "create image",
]


# Lambda functions to combine pre-defined commands and voice commands
is_time_command = lambda command: any(time_command.lower() in command.lower() for time_command in time_cmd)
is_date_command = lambda command: any(date_command.lower() in command.lower() for date_command in date)
is_weather_command = lambda command: any(weather_command.lower() in command.lower() for weather_command in weather_commands)
is_my_name_command = lambda command: any(my_name_.lower() in command.lower() for my_name_ in my_name_qus)
is_routine_command = lambda command: any(routine.lower() in command.lower() for routine in routine_cmd)
is_imgGen_command = lambda command: any(img_command.lower() in command.lower() for img_command in imgGen)



# Main logic of response
def cmd(command):
    if command == "hello":
        return "Hi there!"
    elif is_my_name_command(command):
        return f"Hi, I'm a fun project, which is developed by MeEk_0. Want to know my name ? I'm Pika. Thanks !"
    elif is_time_command(command):
        now = datetime.now()
        return f"The time is {now.strftime('%H:%M')} or {now.strftime('%I:%M %p')}"
    elif is_date_command(command):
        now = datetime.now()
        return f"Today is {now.strftime('%B %d, %Y')}."
    elif is_weather_command(command):
        engine.say("Enter Your City Name : ")
        engine.runAndWait()
        for char in "\nEnter Your City Name : ":
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()
        city = input()
        return f"Weather report, {get_weather(city)}"
    elif is_routine_command(command):
        return f"{routine()}"
    elif is_imgGen_command(command):
        image_description = command.split(maxsplit=1)[1]
        return f"{image_gen(image_description)}"
    elif command == "how are you":
        return "I'm doing well, thank you!"
    else:
        # uncomment bellow line for ChatGPT response but you need to put api key in the environment var
        # return f"{talk(command).strip()}"
        return f"Not Here !"