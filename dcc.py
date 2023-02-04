import speech_recognition as sr

r = sr.Recognizer()

record = sr.AudioFile("dchase.wav")

with record as source:
    # print('Speak Anything : ')
    audio = r.record(source)

try:
    text = r.recognize_google(audio)
    print('You said : {}'.format(text))
except:
    print('Sorry could not recognize your voice')
    
