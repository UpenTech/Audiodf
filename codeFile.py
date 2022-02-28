from asyncore import file_dispatcher
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
if "/Title" in code:
    text += f"""
    Hello, this is the audio version of your 
    pdf and I am Miss Frankie and I will be reciting your document 
    named {name_doc}.\n"""
else:
    pass

total_pages = pdfReader.getNumPages()

if total_pages <= 25:
    pass
else:
    pass