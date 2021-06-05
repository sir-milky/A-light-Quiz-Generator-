import re
import PyPDF2 as pdf
from random import *


def ripPdf (x) :
    pdfHandle = pdf.PdfFileReader(x)
    length = pdfHandle.getNumPages()
    pool = list()

    for x in range(0, length) :
        pdfPage = pdfHandle.getPage(x).extractText()
        extracted = re.findall('[a-zA-z].*?\?',pdfPage)
    
    return(pool)
    


