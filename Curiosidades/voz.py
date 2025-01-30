"""
pip install pyttsx3 -> é uma biblioteca de conversão de texto para fala em Python. Diferentemente de bibliotecas 
alternativas, ela funciona offline e é compatível com Python 2 e 3.

pip install pipwin -> é um pequeno gerenciador de pacotes Python. Ele instala automaticamente pip e virtualenv no 
Windows e sua GUI permite que você: alterne de um interpretador python (ou seja, versão) para outro (incluindo py e pypy )

pip install pyaudio -> 

Agora adicionando mais 5 comandos de voz
Além dos comandos de desligar e cancelar, aqui estão mais 5 comandos úteis:

"Reiniciar o computador" → Reinicia o PC
"Abrir navegador" → Abre o Google Chrome
"Tocar música" → Abre o aplicativo de música do Windows
"Que horas são?" → Diz a hora atual
"Abrir bloco de notas" → Abre o Bloco de Notas

"""

#----------------------------Desligar e Reiniciar o PC por voz--------------------------------

import datetime
import os

import pyttsx3
import speech_recognition as sr


class Comandos:
    
    def assistente_ouvir(self):
        rec = sr.Recognizer()
        with sr.Microphone() as source:
            print('Fale...')
            rec.pause_threshold = 0.6
            audio = rec.listen(source)
            try:
                print('Reconhecendo voz...')
                palavras = rec.recognize_google(audio, language='pt-br').lower()
                print(f"Frase dita: '{palavras}'")
                return palavras
            except sr.UnknownValueError:
                print('Não entendi o que você disse.')
            except sr.RequestError:
                print('Erro ao se conectar ao serviço de reconhecimento de voz.')
            return None
    
    def assistente_falar(self, falar):
        engine = pyttsx3.init()
        engine.say(falar)
        engine.runAndWait()

    def assistente_acoes(self):
        frase = self.assistente_ouvir()
        if frase:
            if 'desligar' in frase:
                print('Quer mesmo desligar?')
                self.assistente_falar('Quer mesmo desligar?')
                decisao = self.assistente_ouvir()
                if decisao and 'sim' in decisao:
                    print('Desligando o computador!')
                    self.assistente_falar('Desligando o computador!')
                    os.system("shutdown /s /t 0")
                else:
                    print('Não vou desligar!')
                    self.assistente_falar('Não vou desligar!')

            elif 'cancelar' in frase:
                print('Cancelando o desligamento...')
                self.assistente_falar('Cancelando o desligamento.')
                os.system("shutdown /a")

            elif 'reiniciar' in frase:
                print('Reiniciando o computador...')
                self.assistente_falar('Reiniciando o computador!')
                os.system("shutdown /r /t 0")

            elif 'abrir navegador' in frase:
                print('Abrindo o Google Chrome...')
                self.assistente_falar('Abrindo o Google Chrome!')
                os.system("start chrome")

            elif 'tocar música' in frase:
                print('Abrindo o aplicativo de música...')
                self.assistente_falar('Abrindo o aplicativo de música!')
                os.system("start ms-music:")

            elif 'que horas são' in frase:
                hora = datetime.datetime.now().strftime("%H:%M")
                print(f"Agora são {hora}")
                self.assistente_falar(f"Agora são {hora}")

            elif 'abrir bloco de notas' in frase:
                print('Abrindo o Bloco de Notas...')
                self.assistente_falar('Abrindo o Bloco de Notas!')
                os.system("notepad")

            else:
                print('Desculpe, não entendi!')
                self.assistente_falar('Desculpe, não entendi!')


if __name__ == '__main__':
    assistente = Comandos()
    assistente.assistente_acoes()
