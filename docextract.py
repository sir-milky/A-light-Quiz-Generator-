import docx 
import re

def documentRip(x) :

    fileHandle = docx.Document(x)
    pool = str()
    for line in fileHandle.paragraphs:
        pool = pool + line.text

    pool = re.sub("_",'',pool)
    rip = re.findall('[a-zA-Z].*?\?',pool)
    return rip

