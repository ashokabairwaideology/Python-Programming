import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('py.pdf', 'rb'))


import pyttsx3
speaker = pyttsx3.init()


for page_num in range(pdfReader.numPages):
    text =  pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()

#Now the next step is to save the audio as mp3 file:
engine = ""
engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()