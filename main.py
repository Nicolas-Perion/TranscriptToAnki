from anki_action import AnkiClient
from config import URL
from download_audio import download_split_by_chapters
from transcript import write_transcriptions

deck = "Data Structures"
client = AnkiClient()

download_split_by_chapters(URL, chapters_to_exclude=["Ad"], split=True)
write_transcriptions()
client.create_deck(deck)
