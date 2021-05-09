from flask import Flask
app = Flask(__name__)

import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import speech_recognition as sr
from gtts import gTTS 
import os 
from playsound import playsound



def capture_face():

    cascPath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    log.basicConfig(filename='webcam.log',level=log.INFO)

    video_capture = cv2.VideoCapture(0)
    anterior = 0

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            if(w>100 and h>100):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                name = "Pravallika"
                cv2.putText(frame, name, (x + 2, y), font, 0.4, (255, 255, 255), 1)
        if anterior != len(faces):
            anterior = len(faces)
            log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
        # Display the resulting frame
        cv2.imshow('Video', frame)

        

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

#capture_face()

def speech_to_text():
    r = sr.Recognizer()

    with sr.AudioFile(file_name) as source:
        audio = r.listen(source)

    try:
        # print("Google Cloud Speech thinks you said " + r.recognize_google(audio))
        result = r.recognize_google(audio)
        return result
    except sr.UnknownValueError:
        print("Google Cloud Speech could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Cloud Speech service; {0}".format(e))


def text_to_speech(text):
    language = 'en'
    myobj = gTTS(text=text, lang=language, slow=False) 
    myobj.save('tts.mp3')
    playsound("tts.mp3")

@app.route('/', methods=['GET'])
def main():
    capture_face()
    #text_to_speech("Can you tell me your favourite place")
    #speech_to_text()
    #return render_template('auth.html')
    #text_to_speech("Can I get your favorite food item")

main()