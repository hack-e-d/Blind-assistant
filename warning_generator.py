from gtts import gTTS 
import os 

def generate_audio(mytext):
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False) 

