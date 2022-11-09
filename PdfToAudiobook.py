import pyttsx3
import PyPDF2

speaker = pyttsx3.init()
book = open('PdfToAudiobook.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
page = pdfReader.getPage(0)
text = page.extractText()
speak = pyttsx3.init()
speak.say(text) 
speak.runAndWait()