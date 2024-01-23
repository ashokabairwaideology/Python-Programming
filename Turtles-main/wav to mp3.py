from os import path
from pydub import AudioSegment

# Enter the filename you want to convert it should in the same folder as this python file
src = "Bewajah_Full_Video_Song___Sanam_Teri_Kasam.mp3"
dst = "output.mp3"

#convert wav to mp3
sound = AudioSegment.from_mp3(src)
sound.export(dst, format="wav")

print("Converted Successfully")