
import speech_recognition as sr
import sys
import time 

r = sr.Recognizer()
print("Please deliver speech and say quit when done: ")
l=0
i=0
time_1=time.time()
time_2=0
while i==0:
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=0.2)
        
        audio = r.listen(source)
        print("Recognizing...")
        try:

            text = r.recognize_google(audio)
            print("Speech: ", text)
            l=l+len(text.split(' '))
            if 'quit' in text:
                time_2=time.time()
                i=1
        except:
            print('Please say clearly!!')
            
if (float(l/(time_2-time_1)))>3: print("Your speech is faster than usual")
elif(0<float(l/(time_2-time_1)))<1: print("Your speech was slower than usual")
else: print("You spoke confidently!")






      
