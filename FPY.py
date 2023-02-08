# Algumas funçoes com Python #
# comprimir PDF com Python #

#PIP INSTALL PYPDF2#

import PyPDF2

def comprimir_pdf(arquivo_entrada, arquivo_saida):
    with open(arquivo_entrada, 'rb') as arquivo:
        pdf = PyPDF2.PdfFileReader(arquivo)
        pdf_escritor = PyPDF2.PsfFileWriter()
        for pagina in range(pdf.getNumPages()):
            pdf_escritor.addPage(pdf.getPage(pagina))
        with open(arquivo_saida, 'wb') as saida:
            pdf_escritor.writer(saida)
            
comprimir_pdf("entrada.pdf", "saida.pdf")

# Remover fundo de uma imagem #

from skimage import io
import numpy as np

imagem = io.imread("entrda.jpg")
img_rgb = imagem(..., :3)
cor_fundo = [255, 255, 255]
mascara = np.all(img_rgb == cor_fundo, axis=-1)
img_mascarada = np.copy(img_rgb)
img_mascarada[mascara] = [0, 0, 0]
io.imsave("saida.png", masked_img, format="png")

# como instalar videos do twitter #

import requests
from bs4 import BeautifulSoup

url = "#"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
video_url = soup.find('meta', {'property': 'og:video'})
['content']

response = requests.get(video_url, stream=True)
open('video.mp4', 'wb').write(response.content)

# criar um instaDownloader #

import requests
from bs4 import BeautifulSoup

response =
requests.get("#")
soup = BeautifulSoup(response.text, 'html.parser')

# audio para texto #

import speech_recognition as sr

r = sr.Recongnicer()

with sr.AudioFile('meuaudio.mp3') as meu_audio:
    audio = r.listen(meu_audio)
    
    try:
        texto  = r.recognize_google(audio_text)
        print(texto)
    except:
        print("tente novamenete")

