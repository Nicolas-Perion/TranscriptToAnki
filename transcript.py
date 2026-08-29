from faster_whisper import WhisperModel
import os
from config import TEMP_AUDIO_DIRECTORY_PATH, TRANSCRIPTIONS_DIRECTORY_PATH, MODEL_SIZE
from pathlib import Path

model = WhisperModel(model_size_or_path=MODEL_SIZE, device="cpu", local_files_only=True)
os.makedirs(name=TRANSCRIPTIONS_DIRECTORY_PATH, exist_ok=True)

def write_transcriptions() :
    chapters_paths = [os.path.join(TEMP_AUDIO_DIRECTORY_PATH, path) for path in os.listdir(TEMP_AUDIO_DIRECTORY_PATH)]
    for chapter_path in chapters_paths :
        segments = model.transcribe(chapter_path)
        segments = segments[0]
        
        transcription_path = str(os.path.join(TRANSCRIPTIONS_DIRECTORY_PATH, Path(chapter_path).stem)) + ".txt"
        with open(transcription_path, "a", encoding="utf-8") as file:
            for segment in segments:
                file.write(segment.text)
    return