import paho.mqtt.client as mqtt  # ler e publicar tópicos mqtt


def controla_luz(comando):
    CLIENT = mqtt.Client()
    CLIENT.connect('localhost')
    CLIENT.publish('cleusa/iluminacao', str(comando))

if __name__ == '__main__':
    controla_luz(1)
    