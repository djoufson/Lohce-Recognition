import speech_recognition as sr
import assemblyai as aai
import json

from utilities.audio import convert_to_wav

class FrenchRecognizer:
    def recognize(self, path):
        r = sr.Recognizer()
        output_path = convert_to_wav(path)
        with sr.AudioFile(output_path) as source:
            audio = r.record(source)

        result = r.recognize_vosk(audio, language="fr")
        return json.loads(result)['text']

    def recognize_assembly(self, path):
        output_path = convert_to_wav(path)
        aai.settings.api_key = "c623f21a00114c67a8e737f051c459ad"
        transcriber = aai.Transcriber()
        response = transcriber.transcribe(output_path)
        return response.text
    
    def recognize_whisper(self, path):
        output_path = convert_to_wav(path)