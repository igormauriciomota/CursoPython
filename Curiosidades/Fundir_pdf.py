"""
(I) Adquirindo código fonte de um site:

import urllib.request

print(urllib.request.urlopen("https://www.youtube.com/").read())

-------------------------//-------------------------------

(II) Fundir PDF's: "C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\Arquivo2.pdf"




"""

# pip install PyPDF2
from PyPDF2 import PdfMerger

merger = PdfMerger()

merger.append("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\Arquivo1.pdf")
merger.append("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\Arquivo2.pdf")

merger.write("C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\Arquivo3.pdf")
merger.close()

print("Os PDF's foram mesclados com sucesso!")

