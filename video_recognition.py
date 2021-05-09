
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

        """video_capture = cv2.VideoCapture(filename)
    length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(video_capture.get(cv2.CAP_PROP_FPS))

    harmesh = face_recognition.load_image_file("face1.jpg")
    hfencoding = face_recognition.face_encodings(harmesh)[0]

    prateek = face_recognition.load_image_file("face2.jpeg")
    pfencoding = face_recognition.face_encodings(prateek)[0]

   
    known_face_encodings = [
        hfencoding,
        pfencoding
    ]
    known_face_names = [
        "Face1",
        "Face2"
    ]

    width  = int(video_capture.get(3)) # float
    height = int(video_capture.get(4))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    PATH = 'C:\\Users\\Pravallika Myneni\\Desktop\\version-2\\demo.mp4'
    out = cv2.VideoWriter(PATH,fourcc, fps, (width,height))
    for i in range(1,length-1):
        
        ret, frame = video_capture.read()
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)"""

        # Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            if(w>100 and h>100):
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                font = cv2.FONT_HERSHEY_DUPLEX
                name = "Pravallika"
                #matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                #name = "Unknown"
                #face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                #best_match_index = np.argmin(face_distances)
                #if matches[best_match_index]:
                    #name = known_face_names[best_match_index]
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

def main():
    capture_face()

main()