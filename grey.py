import speech_recognition as grey

listener = grey.Recognizer()

try:
    with grey.Microphone() as origin:
        print("listening")
        speech = listener.listen(origin)
        instruction = listener.recognize_google(speech)
        print(instruction)


except:
    pass