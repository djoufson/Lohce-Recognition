import moviepy.editor as mp

def convert_to_wav(path):
    output_path = "/home/dk/Downloads/out-put-voice.wav"
    audio_file = mp.AudioFileClip(path)
    audio_file.write_audiofile(output_path)

    return output_path
