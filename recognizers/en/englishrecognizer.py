import speech_recognition as sr
import assemblyai as aai
import json
import whisper

from utilities.audio import convert_to_wav

class EnglishRecognizer:
    def recognize(self, path):
        r = sr.Recognizer()
        output_path = convert_to_wav(path)
        with sr.AudioFile(output_path) as source:
            audio = r.record(source)

        result = r.recognize_vosk(audio)
        return json.loads(result)['text']

    def recognize_assembly(self, path):
        output_path = convert_to_wav(path)
        aai.settings.api_key = "c623f21a00114c67a8e737f051c459ad"
        transcriber = aai.Transcriber()
        response = transcriber.transcribe(output_path)
        return response.text
    
    def recognize_whisper(self, path):
        output_path = convert_to_wav(path)
        model = whisper.load_model("base")
        result = model.transcribe(output_path)
        return result["text"]
