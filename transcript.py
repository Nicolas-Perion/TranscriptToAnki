import os
from pathlib import Path

from faster_whisper import WhisperModel

from config import MODEL_TRANSCRIPTION_SIZE

model = WhisperModel(
    model_size_or_path=MODEL_TRANSCRIPTION_SIZE, device="cpu", local_files_only=True
)
os.makedirs(name="transcriptions", exist_ok=True)


def write_transcriptions():
    """Write transcriptions of the audio extract in the ./temp_audio/ folder."""
    chapters_paths = [p for p in Path("./temp_audio").iterdir() if p.is_file()]

    for chapter_path in chapters_paths:
        segments = model.transcribe(str(chapter_path))
        segments = segments[0]

        transcription_path = (
            str(os.path.join("./transcriptions/", chapter_path.stem)) + ".txt"
        )
        with open(transcription_path, "a", encoding="utf-8") as file:
            for segment in segments:
                file.write(segment.text)
    return
