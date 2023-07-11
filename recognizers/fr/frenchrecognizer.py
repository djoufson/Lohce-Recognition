import speech_recognition as sr
import moviepy.editor as mp

class FrenchRecognizer:
    def recognize(self, path):
        r = sr.Recognizer()
        audio_file = mp.AudioFileClip(path)
        audio_file.write_audiofile("D:/Work Folder/Open Source/Djoufson/LohceRecognition/out/voice.wav");
        with sr.AudioFile("../../out/voice.wav") as source:
            audio = r.record(source)
        result = r.recognize_vosk(audio, language="fr")
        return result
