import os
import shutil

from anki_action import AnkiClient
from download_audio import download_split_by_chapters
from transcript import write_transcriptions
from write_cards_content import write_cards_content


def cleanup_temp_files():
    """Nettoyer les fichiers temporaires."""
    if os.path.exists("./temp_audio/"):
        shutil.rmtree("./temp_audio/")
        os.makedirs("./temp_audio/", exist_ok=True)
    if os.path.exists("./transcriptions/"):
        shutil.rmtree("./transcriptions/")
        os.makedirs("./transcriptions/", exist_ok=True)


# Nettoyage initial
cleanup_temp_files()

url = "https://youtu.be/vVL6NFzr0Rg"
deck = "Data Structures"
client = AnkiClient()

download_split_by_chapters(url, chapters_to_exclude=["Ad"], split=True)
write_transcriptions()
client.create_deck(deck)

for transcription_file in os.listdir("./transcriptions/"):
    transcription_path = os.path.join("./transcriptions/", transcription_file)
    card_content = write_cards_content(transcription_path)
    client.create_cards(deck, card_content)

print("\n✓ Toutes les cartes ont été créées avec succès!")
print("Vous pouvez maintenant consulter votre deck dans Anki.")
