from gtts import gTTS
from subprocess import call


def cria_audio(texto: str, nome_arquivo: str) -> None:
    tts = gTTS(texto, lang='pt-br')
    tts.save(f'audios/{nome_arquivo}.mp3')
    call(['mpg123', '-q', f'audios/{nome_arquivo}.mp3'])


if __name__ == '__main__':
    cria_audio('Fala comigo Xandão', 'feedback')
