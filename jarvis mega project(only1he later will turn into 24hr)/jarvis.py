import speech_recognition as sr
import pyttsx3
import webbrowser
import subprocess
import datetime
import os
import pyaudio
# Initialize text-to-speech engine
engine = pyttsx3.init()

# Speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen for a command
def listen(prompt=False):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        if prompt:
            speak("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            return command.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

# Process the recognized command
def process_command(command, in_weapon_mode=False):
    if not command:
        speak("Sorry, I didn't catch that.")
    else:
        speak(f"You said: {command}")
        if 'hello' in command:
            speak("Hello! How can I help you today?")
        elif 'date' in command or 'time' in command:
            now = datetime.datetime.now()
            current_time = now.strftime("%Y-%m-%d %H:%M:%S")
            speak(f"The current date and time is {current_time}")
        elif 'play music' in command:
            speak("Playing your favorite music.")
        elif 'search for' in command:
            search_query = command.replace('search for', '').strip()
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Searching for {search_query}")
        elif 'open' in command:
            app = command.replace('open', '').strip().lower()
            open_app(app)
        elif 'enter weapon' in command:
            speak("Please provide the password to enter weapon mode.")
            password = listen(prompt=True)
            if password == 'delta':
                speak("Entering weapon mode.")
                print("Entering weapon mode.")
                weapon_mode()
            else:
                intruder_detected()
        elif 'lockdown' in command:
            speak("Please provide the lockdown password.")
            password = listen(prompt=True)
            if password == 'delta':
                lock_computer()
            else:
                speak("Incorrect password.")
        elif 'shutdown' in command:
            secure_command("shutdown")
        elif 'hibernate' in command:
            secure_command("hibernate")
        elif 'sleep' in command:
            secure_command("sleep")
        elif in_weapon_mode:
            if 'command1' in command:
                speak("Executing command 1.")
                # Add command 1 action
            elif 'command2' in command:
                speak("Executing command 2.")
                # Add command 2 action
            elif 'nuclear missile' in command:
                speak("Please provide the nuclear password.")
                nuke_password = listen(prompt=True)
                if nuke_password == 'delta':
                    speak("Where would you like to launch the missile?")
                    target = listen(prompt=True)
                    speak(f"Launching to {target}.")
                else:
                    intruder_detected()
            # Add more weapon mode commands as needed
            
            # Clear console and start from the beginning
            clear_console()
            main_loop()
        else:
            speak("Sorry, I can't comply with that command.")

# Open specific applications
def open_app(app_name):
    try:
        if 'notepad' in app_name:
            subprocess.Popen(['notepad.exe'])
            speak("Opening Notepad")
        elif 'calculator' in app_name:
            subprocess.Popen(['calc.exe'])
            speak("Opening Calculator")
        elif 'chrome' in app_name:
            subprocess.Popen(['chrome.exe'])
            speak("Opening Chrome")
        else:
            speak("I can't open that application.")
    except Exception as e:
        speak(f"Sorry, I couldn't open the application. {str(e)}")

# Lock the computer
def lock_computer():
    if os.name == 'nt':  # Check if the operating system is Windows
        subprocess.call('rundll32.exe user32.dll, LockWorkStation')

# Intruder detected functionality
def intruder_detected():
    speak("Intruder detected, entering lockdown mode.")
    lock_computer()

# Weapon mode functionality
def weapon_mode():
    in_weapon_mode = True
    while in_weapon_mode:
        command = listen(prompt=True)
        process_command(command, in_weapon_mode)
def secure_command(command_type):
    speak(f"Please provide the password for {command_type}.")
    password = listen(prompt=True)
    if password == 'delta':
        if command_type == "shutdown":
            speak("Shutting down the system.")
            os.system("shutdown /s /t 0")
        elif command_type == "hibernate":
            speak("Hibernating the system.")
            os.system("shutdown /h")
        elif command_type == "sleep":
            speak("Putting the system to sleep.")
            os.system("rundll32.exe powrprof.dll,SetSuspendState Sleep")
    else:
        speak("Incorrect password. Action denied.")
# Clear the console
def clear_console():
    if os.name == 'nt':
        os.system('cls')

# Main loop function
def main_loop():
    while True:
        clear_console()
        print("Listening...")
        wake_word = listen(prompt=True)
        if 'jarvis' in wake_word:
            speak("Wake word detected.")
            print("Wake word detected.")
            speak("Listening...")
            print("Listening...")
            command = listen(prompt=False)
            process_command(command)
if __name__ == "__main__":
    main_loop()