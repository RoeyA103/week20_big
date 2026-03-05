import speech_recognition as sr

class VoiceExtractor():
    def __init__(self,logger):
        self.logger = logger
        self.r = sr.Recognizer() 

        self.logger.info("VoiceExtractor - created")

    def extract_text(self,file)->str:
        harvard = sr.AudioFile(file)
        with harvard as source:
            audio = self.r.record(source)

        text = self.r.recognize_google(audio_data=audio)

        self.logger.debug("VoiceExtractor - text extracted successfuly")

        return text

