# Jarvis 
import musicLibrary
import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
from gtts import gTTS
import pygame

import os
from dotenv import load_dotenv

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "52f78136fff445bb80d90f0a8a4d155e"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize Pygme mixer
    pygame.mixer.init()

    #Load the mP# file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the mp3 file
    pygame.mixer.music.play()

    # Keep the program running untll the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    
#Using deepseek api
def aiProcess(command):
    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
        }
        
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Assistant."},
                {"role": "user", "content": command}
            ]
        }
        
        response = requests.post(
            "https://api.deepseek.com/v1/chat/completions",
            headers=headers,
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            return f"API Error: {response.status_code} - {response.text}"
            
    except Exception as e:
        return f"Error processing request: {str(e)}"

def processCommand(c):
    print(c)
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open facebook" in c:
        webbrowser.open("https://facebook.com")
    elif "open gmail" in c:
        webbrowser.open("https://gmail.com")
    elif "open twitter" in c:
        webbrowser.open("https://twitter.com")
    elif "open youtube" in c:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c:
        webbrowser.open("https://linkedin.com")

    elif c.startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)


    elif "news" in c:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response 
            data = r.json()

            # Extract the articles
            articles = data.get('articles', [])

            #Print the headlines
            for article in articles:
                # print(article['title'])
                speak(article['title'])

    else:
        #Let openAI handle the request
        output = aiProcess(c)
        speak(output)
        pass




if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        
        #Lister for the word "Jarvis"
        r = sr.Recognizer()
        print("recognizing...")
        try: 
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=3, phrase_time_limit=1)
            word = r.recognize_google(audio)
            # Change this in your main loop
            if word.lower() == "jarvis":
                speak("Yes sir! How may I help you?")
                try:
                    with sr.Microphone() as source:
                        recognizer.adjust_for_ambient_noise(source)
                        print("Jarvis Active...")
                        audio = recognizer.listen(source, timeout=5)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)
                except sr.WaitTimeoutError:
                    speak("I didn't hear any command, sir.")
                    continue

        except sr.UnknownValueError:
            print("Jarvis could not understand the audio.")


        except Exception as e: 
            print("Error: {0}".format(e))
            