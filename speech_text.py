import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import speech_recognition as sr
from gtts import gTTS 
import os 
from playsound import playsound


def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        try:
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print("Answer: "+ text) 
        except:
            print("Sorry, I did not get that")
    return text

def text_to_speech(text, file_name):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save(file_name)
    playsound(file_name)

@app.route('/', methods=['GET'])
def main():
    text_to_speech("What is the name of your first pet", 'qn1.mp3')
    speech_to_text()
    text_to_speech("What city were you born", 'qn2.mp3')
    speech_to_text()
    text_to_speech("What was the first name of your first roommate", 'qn3.mp3')
    speech_to_text()
    #return render_template('auth.html')
    #text_to_speech("Can I get your favorite food item")

main()