from faster_whisper import WhisperModel
import os
from config import MODEL_SIZE
from pathlib import Path

model = WhisperModel(model_size_or_path=MODEL_SIZE, device="cpu", local_files_only=True)
os.makedirs(name="transcriptions", exist_ok=True)


def write_transcriptions():
    chapters_paths = [
        os.path.join("./temp_audio/", path)
        for path in os.listdir(TEMP_AUDIO_DIRECTORY_PATH)
    ]
    for chapter_path in chapters_paths:
        segments = model.transcribe(chapter_path)
        segments = segments[0]

        transcription_path = (
            str(os.path.join("./transcriptions/", Path(chapter_path).stem)) + ".txt"
        )
        with open(transcription_path, "a", encoding="utf-8") as file:
            for segment in segments:
                file.write(segment.text)
    return
