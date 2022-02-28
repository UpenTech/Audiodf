from PyPDF2 import PdfFileReader
from gtts import gTTS

FILE_SOURCE = input("Location of your pdf file: ")
#FILE_DESTINATION = input("Where do you want to store the file?\n>")

pdfFILE = open(FILE_SOURCE,"rb")
pdfReader = PdfFileReader(pdfFILE)

text = ""

code = pdfReader.getDocumentInfo()
name_doc = FILE_SOURCE[0:FILE_SOURCE.index(".")]

print(code)


import pyttsx3
common = pyttsx3.init()


if "/Title" in code:
    common.say(f"Hello, this is the audio version of your" \
    + "pdf and I am Miss Frankie and I will be reciting your document" \
    + "named {name_doc}.\n")

    common.runAndWait()
else:
    common.say(f"Hello, this is the audio version of your" \
    + "pdf and I am Miss Frankie and I will be reciting your document")
    common.runAndWait()
    

total_pages = pdfReader.getNumPages()


if total_pages <= 25:
    for i in range(0, total_pages):
        text += pdfReader.getPage(i).extractText()
    
    gTTS(text, lang='en').save("file.mp3")
    common.say("Your pdf has successfully been converted to mp3 and has been saved.")
    common.runAndWait()
else:
    common.say("Your pdf file contains too many pages.")
    common.runAndWait()
