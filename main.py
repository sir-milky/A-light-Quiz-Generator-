from pdfextract import ripPdf
from docextract import documentRip
import os
import random 

path = input("Enter path of the files to strip: ")
files = os.listdir(path)
totalPool = list()

print("Displaying the current list of files detected...", files)

for file in files :
    if file.endswith('.pdf') :
        pdfPool = ripPdf(path + file)
        totalPool = totalPool + pdfPool
        print(pdfPool)
    elif file.endswith('.docx') :
        docPool = documentRip(path + file)
        totalPool = totalPool + docPool

print(totalPool)
while True :
    print(totalPool[random.randint(0,len(totalPool)-1)])
    answer = input("Answer? ")
