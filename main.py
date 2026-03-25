import speech_recognition as sr

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)

        try:
            command = r.recognize_google(audio)
            print("You said:", command)

            if "open" in command:
                print("Opening robotic hand")
            elif "close" in command:
                print("Closing robotic hand")

        except:
            print("Could not understand")

listen_command()
