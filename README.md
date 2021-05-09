# Reimagining Service Canada -- Face and Voice Verification
Increasing Inclusivity In the Digital Identity Lifecycle! 


# How does this work:
video_recognition.py -> for facial recognition in video_capture
speech_text -> it reads out the security questions and fills them with the answers given by user through speech



## Problem
All of these digital interactions echo a frustrating experience that’s familiar to many, and exclude the needs of a considerable part of the population. Individuals without sufficient technological knowledge or those who aren't tech-savvy struggle to access important digital spaces because of lack of ease and accessibility. Most two-factor or multi-factor authentication services also fail to consider groups of users without dedicated mobile phones or consistent access to technology.
## What it does

We redesigned Service Canada's website to integrate a more inclusive security authentication feature within the GCKey service. The user will first register their facial features and voice while responding to chosen security questions. This data is then used to accurately recognize the user during future log-ins. Instead of struggling to receive a code, email or voice message, they can simply respond to the questions they're asked through the webcam, like a casual conversation! No secondary device or additional steps needed.

By integrating the digital identity of an individual with their real-life biology, we aim to reduce the security and authentication barrier for those with limited technological access and ability. With considerations for painless user experience, the redesign also allows an accurate, secure process for users who worry about credential attacks. 

## How we built it
We made a working design prototype of the Setup and Sign-in flow on Figma. We developed the front end using HTML and CSS, and the backend with flask (python). The main modules involved are OpenCV for face recognition, speech_recognition for speech to text, and gTTS for Text to Speech.
## Challenges we ran into
1. Digital identity / security was a topic none of us were familiar with, so a lot of research and questions were necessary for understanding the challenge.
2. Developing the algorithm for facial recognition was very new to us, which meant we ran into many errors!
3. One of major difficulties was to perform video capture, Speech to Text and Text to Speech modules in a concurrent manner. 

## Accomplishments that we're proud of
Our team members are located in three different time zones, consisting of one developer and three designers. The lack of time and imbalance between developing and designing meant we had to manage our time as best as possible, and be considerable to each other's schedules / skillsets! Through great teamwork, we were able to work comfortably together. 

## What's next for Face and Voice Verification
High-security biometric facial recognition has great advantages compared to, for example, OTP by email or SMS, which can be hacked more easily — or fingerprint recognition, which requires a fingerprint reader that is not present in all electronic devices. Tying digital access to physical characteristics in this way increases cybersecurity and convenience by ensuring that a person’s digital world is being accessed by the correct person.
