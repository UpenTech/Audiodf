from PyPDF2 import PdfFileReader
from gtts import gTTS
import pyttsx3
from colorama import Fore

common = pyttsx3.init()
common.setProperty("rate",155)

FILE_SOURCE = input("Location of your pdf file: ")
#FILE_DESTINATION = input("Where do you want to store the file?\n>")
try:
    pdfFILE = open(FILE_SOURCE,"rb")
    pdfReader = PdfFileReader(pdfFILE)

    text = ""

    code = pdfReader.getDocumentInfo()
    name_doc = FILE_SOURCE[0:FILE_SOURCE.index(".")]

    print(code)

    common.say(f"Hello, this is the audio version of your" \
    + " pdf file and I am Mister Frank and Miss Frankie will be reciting your document")
    common.runAndWait()
        

    total_pages = pdfReader.getNumPages()


    if total_pages <= 25:
        for i in range(0, total_pages - 20):
            text += pdfReader.getPage(i).extractText()
        
        print(Fore.BLUE + "Converting to mp3..." + Fore.YELLOW +" This may take a while depending upon your file size ." + Fore.RESET)
        gTTS(text, lang='en', slow=False).save("file.mp3")
        common.say("Your pdf has successfully been converted to mp3.")
        common.runAndWait()

    else:
        common.say("Your pdf file contains too many pages.")
        common.runAndWait()

except IOError:
    common.say("File not found")
    common.runAndWait()
