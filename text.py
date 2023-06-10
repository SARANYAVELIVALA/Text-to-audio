from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
z=input("enter your text:")
language='en'
print("----------audio is playing------------")
sp=gTTS(text=z,lang=language,slow=False)
sp.save(audio)
playsound(audio)

