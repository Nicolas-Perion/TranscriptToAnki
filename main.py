import os

from anki_action import AnkiClient
from config import URL
from download_audio import download_split_by_chapters
from transcript import write_transcriptions
from write_cards_content import write_cards_content

deck = "Data Structures"
client = AnkiClient()

download_split_by_chapters(URL, chapters_to_exclude=["Ad"], split=True)
write_transcriptions()
client.create_deck(deck)

for transcription_path in os.listdir("./transcriptions/"):
    card_content = write_cards_content(transcription_path)
    client.create_cards(deck, card_content)
