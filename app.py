from app import speech_text
from app import video_recognition

import os 
import sys
from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)



@app.route("/")
def index():
    return render_template('auth.html')

@app.route("/1")
def actual_work():
    path = "C:\\Users\\Pravallika Myneni\\Desktop\\tohacks\\static\videocapture.mp4"
    ##the video captured from auth.html
    video_recognition.capture_face()

    #from the list of security questions
    text_to_speech("What is the name of your first pet", 'qn1.mp3')
    q1_ans = speech_to_text()
    print(q1_ans)
    text_to_speech("What city were you born", 'qn2.mp3')
    q2_ans = speech_to_text()
    print(q2_ans)
    text_to_speech("What was the first name of your first roommate", 'qn3.mp3')
    q3_ans = speech_to_text()
    print(q3_ans)

    return [q1_ans, q2_ans, q3_ans]

    ##future work is to implement this function in forms real-time
    



    


