'''______________________________Abrindo aplicativos usando a voz______________________________'''

# # Abrindo aplicativos usando a voz
#
# # pip install pyttsx3, SpeechRecognition
# # PyAudio -> pip install pipwin -> pipwin install pyaudio
# from pyttsx3 import init
# from speech_recognition import Recognizer, Microphone
# from os import system
#
# class Comandos:
#
#     def assistente_ouvir(self):
#         rec = Recognizer()
#         with Microphone() as source:
#             print('Fale...')
#             rec.pause_threshold = 0.6
#             audio = rec.listen(source)
#             try:
#                 print('Reconhecendo voz...')
#                 palavras = (rec.recognize_google(audio, language='pt-br')).lower()
#                 print(f"Frase dita: '{palavras}'")
#             except:
#                 print('_____Não estou ouvindo!')
#                 return 'None'
#         return palavras
#
#     def assistente_falar(self, falar):
#         engine = init('sapi5')
#         engine.say(falar)
#         engine.runAndWait()
#
#     def assistente_acoes(self):
#         while True:
#             frase = self.assistente_ouvir()
#             if frase != 'None':
#                 if "bloco de notas" in frase:
#                     print("_____Abrindo bloco de notas!")
#                     self.assistente_falar("Abrindo bloco de notas!")
#                     system("start notepad")
#
#                 elif "navegador" in frase:
#                     print("_____Abrindo navegador!")
#                     self.assistente_falar("Abrindo navegador!")
#                     system("start firefox")
#
#                 elif "arquivos" in frase:
#                     print("_____Abrindo arquivos!")
#                     self.assistente_falar("Abrindo arquivos!")
#                     system("start explorer")
#
#                 elif 'cmd' in frase:
#                     print("_____Abrindo CMD!")
#                     self.assistente_falar("Abrindo CMD!")
#                     system("start cmd")
#
#
# if __name__ == '__main__':
#     assistente = Comandos()
#     assistente.assistente_acoes()