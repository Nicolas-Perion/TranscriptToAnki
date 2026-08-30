URL = "https://youtu.be/vVL6NFzr0Rg?si=uS-n4RibJY1hIyaj"
TEMP_AUDIO_DIRECTORY_PATH = "/home/nicolas/Projets DS/TranscriptToAnki/temp_audio"
TRANSCRIPTIONS_DIRECTORY_PATH = (
    "/home/nicolas/Projets DS/TranscriptToAnki/transcriptions"
)
COOKIES_PATH = "/home/nicolas/Projets DS/TranscriptToAnki/cookies.txt"
DENO_PATH = "/usr/bin/deno"
MODEL_SIZE = "tiny.en"  # See https://huggingface.co/collections/Systran/faster-whisper for available models but 'tiny.en' is doing pretty good

MODEL = "llama3.2:3b"
SYSTEM_PROMPT = """
You are an Anki card creator.
You will receive information about a topic and must generate content for the fields of
of the card associated with this topic.
"""
