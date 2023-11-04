from PyPDF2 import PdfReader
import pyttsx3

pdf_reader = PdfReader("textrap.pdf")

speaker = pyttsx3.init()

for page in pdf_reader.pages:
    text = page.extract_text()
    speaker.say(text)

speaker.runAndWait()
speaker.stop()
