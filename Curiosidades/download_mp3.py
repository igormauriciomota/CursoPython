"""
Webcam, download mp3 e graficos 3D

https://www.youtube.com/watch?v=w3viBe2Q0P8

"C:\\0001-Documentos\\07-PYTHON\\03-Musica"


"""
import os
import time

from moviepy.editor import AudioFileClip
from pytube import YouTube
from tqdm import tqdm


# Função para mostrar barra de progresso
def progresso_barra():
    for _ in tqdm(range(100), desc="Convertendo MP4 para MP3...", ncols=100):
        time.sleep(0.02)

# Entrada do usuário
link = input("Digite o link do vídeo do YouTube: ")
caminho = input("Digite o diretório para salvar o arquivo: ")

yt = YouTube(link)
audio_stream = yt.streams.filter(only_audio=True).first()
mp4_path = audio_stream.download(caminho)

# Nome do arquivo MP3 baseado no título
mp3_path = os.path.splitext(mp4_path)[0] + ".mp3"

# Exibe barra de progresso
progresso_barra()

audio = AudioFileClip(mp4_path)
audio.write_audiofile(mp3_path)
audio.close()

os.remove(mp4_path)

print(f"Conversão concluída! MP3 salvo em: {mp3_path}")
