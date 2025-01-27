"""
Fundir Pdfs alarme e código de sites

1) Alarme

"""

import datetime
import time
from tkinter import *  # Responsavel pela criação da interface, importamos todas funçoes

from playsound import playsound  # Responsavel pelo sinal sonoro pip install playsound

root = Tk() # Defineção do objeto da interface - faz parte do tkinter
root.geometry('500x250') # Define o tamanho do objeto

def alarme(): # Função para impressão da hora atual e hora do alarme
    while True:
        fixar_tempo_alarme = f"{hora.get()}:{minuto.get()}:{segundo.get()}" # Tempo escolhido pelo usuario, o get serve para reconhecer
        tempo_atual = datetime.datetime.now().strftime("%H:%M:%S")#Tempo atual
        time.sleep(1) # Delay para melhorar imprimir de 1 em 1 segundos a contagem
        print(tempo_atual,fixar_tempo_alarme) # Impressao dos tempos
        if tempo_atual == fixar_tempo_alarme: # Caso chegue hora do alarme
            print("Alarme Ativado") # Aviso
            # "C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\dark-night.mp3"
            playsound('C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\darknight.mp3') #Ativa o sinal sonoro e para o loop
            break
        
Label(root,text='Alarme',font=('Arial',25),fg='Gray').place(x=200,y=0) # Armazena um texto na interface com fonte e cor, o place
Label(root,text='Defina o tempo que o alarme irá tocar:',font=('Arial',12),fg='Red').place(x=125,y=50)

hora=StringVar(root) # Criação das variaveis strings na interface
horas =['00','01','02','03','04','05','06','07','08','09','10','11','12',
        '13','14','15','16','17','18','19','20','21','22','23','24'] # Armazenando opçoes
hora.set(horas[0])
h = OptionMenu(root,hora,*horas)
h.place(x=125,y=100)

minuto=StringVar(root)
minutos = ('00','01','02','03','04','05','06','07','08','09','10','11','12',
            '13','14','15','16','17','18','19','20','21','22','23','24',
            '25','26','27','28','29','30','31','32','33','34','35','36',
            '37','38','39','40','41','42','43','44','45','46','47','48','49',
            '50','51','52','53','54','55','56','57','58','59')
minuto.set(horas[0])
m = OptionMenu(root,minuto,*minutos)
m.place(x=230,y=100)

segundo=StringVar(root)
segundos = ('00','01','02','03','04','05','06','07','08','09','10','11','12',
            '13','14','15','16','17','18','19','20','21','22','23','24',
            '25','26','27','28','29','30','31','32','33','34','35','36',
            '37','38','39','40','41','42','43','44','45','46','47','48','49',
            '50','51','52','53','54','55','56','57','58','59')
segundo.set(segundos[0])
s = OptionMenu(root,segundo,*segundos)
s.place(x=330,y=100)


Button(root,text='confirmar',font=('Arial',12),fg='green',command=alarme).place(x=210,y=150) # Definição do botoo de confirmação
root.mainloop() # Manter o alarme ativado


