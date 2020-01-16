from gtts import gTTS 
import os 
from playsound import playsound

#Function definition
def playSong(mood):
    playsound(mood)

def textToSpeech():
    mytext=""
    option=int(input("Enter your option: \n 1-to read from file \n 2-to enter the text as input"))
    if(option==2):
        mytext=input("Enter text :")
    elif(option==1):
        file1 = open(r"text_input/1.txt","r")
        mytext=file1.read() 
        file1.close() 

    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named  
    out="output_audio/7.mp3"
    myobj.save(out) 
    #Playing audio
    print("Playing audio.....")
    playSong(out)

textToSpeech()