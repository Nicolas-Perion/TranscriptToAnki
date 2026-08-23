# Pour modifier cela, voir https://github.com/SYSTRAN/faster-whisper
import whisper
import os
from config import TEMP_AUDIO_DIRECTORY_PATH, TRANSCRIPTIONS_DIRECTORY_PATH
from pathlib import Path

def write_transcriptions() :
    model = whisper.load_model('tiny.en')
    chapters_paths = [os.path.join(TEMP_AUDIO_DIRECTORY_PATH, path) for path in os.listdir(TEMP_AUDIO_DIRECTORY_PATH)]
    for chapter_path in chapters_paths :
        result = model.transcribe(chapter_path, fp16=False)
        
        with open(os.path.join(TRANSCRIPTIONS_DIRECTORY_PATH, Path(chapter_path).name), "w", encoding="utf-8") as file:
            file.write(result['text'])

if __name__ == '__main__':
    write_transcriptions()