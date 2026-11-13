COOKIES_PATH = "/home/nicolas/Projets DS/TranscriptToAnki/cookies.txt"
DENO_PATH = "/usr/bin/deno"
MODEL = "llama3.2:3b"
MODEL_TRANSCRIPTION_SIZE = "tiny.en"  # See https://huggingface.co/collections/Systran/faster-whisper for available models but 'tiny.en' is doing pretty good


URL = "https://youtu.be/vVL6NFzr0Rg"
DECK = "Data Structures"
BUNDLE_SIZE = 2

SYSTEM_PROMPT = """
You are an Anki card creator.
You will receive information about a topic and must generate content for the fields
of the card(s) and be compliant with the provided JSON schema.
All the content you generate must be in english.

Here are more details regarding the content that must appear in each field you may encounter:
- Front : Short question (at most 10 words)
- Back : Answer to that question
"""

SESSION_PROMPT = f"""
You will receive information about the different existing data structures.
For each of them, I want you to generate {BUNDLE_SIZE} cards :
- The first card contains a question and an answer about the formal definition and technical details of the structure.
For example :
Front : What is an array ?
Back : An array is a linear data structure that stores elements of the same data type in contiguous memory locations. It enables instant read but its size is fixed and cannot be changed.

- The second card contains a question and an answer about a use case where this data structure is relevant.
For example :
Front : When is it useful ? Give an example.
Back : It is very useful when instant access is needed and collection size is fixed. For instance, lookup tables for enum-like values (days = ["Monday", "Tuesday", ...]).
"""
