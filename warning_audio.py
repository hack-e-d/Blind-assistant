from gtts import gTTS 
import os 
from pygame import mixer
from tempfile import TemporaryFile

def alert(mytext):
    language = 'en'

    myobj = gTTS(text=mytext, lang=language, slow=False) 

    # Saving the converted audio in a mp3 file named  
    mixer.init()
    sf = TemporaryFile()
    myobj.write_to_fp(sf)
    sf.seek(0)
    mixer.music.load(sf)
    mixer.music.play()
    

