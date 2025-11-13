from gtts import gTTS
import os
text = input("type to speak")
audio = gTTS(text, lang = "es")
audio.save("audio1.mp3")
os.system("audio1.mp3")