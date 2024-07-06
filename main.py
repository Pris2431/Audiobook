# first install packages by using pip install pyttsx3
# for the pdf scanner, download using pip install PyPDF2
import pyttsx3
import PyPDF2

book= open('sample.pdf', 'rb') #you can change 'book' and change the sample.pdf to your pdf file name
pdfReader = PyPDF2.PdfFileReader(book)
pages  = pdfReader.numPages #check number of pages in the pdf file
print(pages)

speaker = pyttsx3.init()
for num in range(7, pages): #change the range to the number of pages you want to read
    page = pdfReader.getPage(7)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
# speaker.say("Hi, sexy! Whare are your plans tonight?")


