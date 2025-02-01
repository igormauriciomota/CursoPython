"""
-----Manuscrever texto-----

pip install pywhatkit==4.6

"""

# Transcrição de texto para manuscrito

#pip install pywhatkit
import pywhatkit as kit

kit.text_to_handwriting(
    'Nome: Roberto\nDisciplina: Física\nExperimento: Lei da Gravidade',
    save_to='C:\\Users\\Igor\\Envs\\CursoPython\\CursoPython\\Curiosidades\\fisica.png',
    rgb=(128, 0, 128)
) 

