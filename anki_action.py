import json

import requests as re


def post_request(action: str, params: dict = {}) -> dict:
    """POST request to http://localsend:8765.

    Args:
        action (str): AnkiWeb action.
        params (dict, optional): Parameters corresponding to the action. Defaults to None.

    Returns:
        dict: Response from the API.
    """
    request = json.dumps({"action": action, "version": 6, "params": params})
    response = re.post(url="http://localhost:8765", data=request)
    return response.json()


class AnkiClient:
    def __init__(self) -> None:
        print("=" * 50)
        try:
            version = post_request("version")
            print(f"✓ Connexion à AnkiConnect réussie (Version: {version['result']})")
        except Exception as e:
            print(f"✗ Échec de connexion à AnkiConnect: {e}")
            print("Vérifiez que Anki est lancé avec l'add-on AnkiConnect")
            raise

    def create_deck(self, deck: str) -> None:
        """Create a deck in Anki, if it doesn't already exists.

        Args:
            deck (str): Name of the deck to create.
        """
        if deck.lower() in [
            existing_decks.lower() for existing_decks in post_request("deckNames")
        ]:
            print("A deck with the same name already exists")
            return
        else:
            new_deck = post_request("createDeck", {"deck": deck})
            if new_deck["error"] is None:
                print("Deck successfully created.")
            else:
                print(f"Error: {new_deck['error']}")
            return

    def create_cards(
        self, deck: str, content: dict[str, str], model: str = "Basic"
    ) -> None:
        """Create one (or several) cards based on the provided model.

        Args:
            deck (str): Deck to create the card(s) into.
            content (dict[str]): Content in the fields corresponding to the model.
            model (str, optional): Model to create the card(s) from. Defaults to "Basic".
        """
        new_card = post_request(
            "addNote",
            {
                "note": {
                    "deckName": deck,
                    "modelName": model,
                    "fields": content,
                },
            },
        )

        if new_card["error"] is None:
            print("Card successfully created.")
        else:
            print(f"Error: {new_card['error']}")
