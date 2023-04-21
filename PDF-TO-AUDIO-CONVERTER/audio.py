import PyPDF3
import pyttsx3
import pdfplumber

file = ''
book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

#You'll have to save the pdf into your working directory.
 
pages = pdfReader.numPages

finalText = ''

with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

# If you want to recite the pdf instead of reading it use:

engine = pyttsx3.inint()
engine.save_to_file(finalText, '')
engine.runAndWait()        
 
