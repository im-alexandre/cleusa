import speech_recognition as sr
from subprocess import call
from corona import corona_virus
from audios.cria_audios import cria_audio
from previsao_tempo import previsao
import os

NOME = 'Cleusa'

trigger = NOME.lower()


def monitora_microfone():
    # obtain audio from the microphone
    microfone = sr.Recognizer()
    
    with sr.Microphone() as source:
        microfone.energy_threshold = 90000
        microfone.adjust_for_ambient_noise(source)
        print(microfone.energy_threshold)
        print("Aguardando Comando")
        audio = microfone.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        entrada = microfone.recognize_google(audio, language='pt-BR')
        entrada = entrada.lower()
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("""Could not request results from Google
        Speech Recognition service; {0}""".format(e))

    else:
        if trigger in entrada:
            print('Comando:', entrada.replace(trigger, ''))
            cria_audio(entrada.replace(trigger, ''), 'entrada')
            # responde()
            executa_comandos(entrada)

    return trigger


def responde(arquivo: str) -> None:
    call(['mpg123', '-q', f'audios/{arquivo}.mp3'])


def executa_comandos(comando: str) -> None:
    if 'coronavirus' in comando:
        dados = corona_virus()
        cria_audio(dados, 'corona')

    if 'tempo' in comando:
        cria_audio(previsao(), 'tempo')

    if 'programar' in comando:
        fala = """
        Legal!
        Mas antes, vamos precisar de música.
        """
        cria_audio(fala, 'música')
        call('./spotify.sh')

    if 'dormir' in comando:
        fala = """
        Tudo bem, por hoje já deu mesmo
        """
        cria_audio(fala, 'dormir')
        exit()


def main():
    monitora_microfone()


if __name__ == '__main__':
    while True:
        main()
