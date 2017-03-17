#RECONHECIMENTO DE VOZ
#
#Requerido: python 3 - Módulos: pyaudio, speech_recognition
#
# OBTENHA A APP-KEY EM https://www.microsoft.com/cognitive-services/en-us/speech-api
# Em Março-2017 havia uma oferta de 5000 chamadas gratuitas
#
import speech_recognition as sr

frase = ""

while (frase.lower() != "fechar"):
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando fala:")
        audio = r.listen(source)

    
    BING_KEY = "[INSERT KEY HERE]" # Microsoft Speech API keys 32-character lowercase hexadecimal strings
    try:
        frase = r.recognize_bing(audio, key=BING_KEY, language="pt-BR")
        print("Você disse: " + frase)
    except sr.UnknownValueError:
        print("Microsoft Speech não entendeu seu audio")
    except sr.RequestError as e:
        print("Microsoft Speech retornou o erro: {0}".format(e))