import pyttsx3

DEAFULT_VOICE = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0'

def create_speech(text: str, out: str, voice: str=DEAFULT_VOICE):
    engine = pyttsx3.init()
    engine.setProperty('voice', voice)
    engine.setProperty('rate', 150)
    engine.save_to_file(text, out)
    engine.runAndWait()
    return out


if __name__ == "__main__":
    
    pass