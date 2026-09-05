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
        version = post_request("version")
        print(f"Version of AnkiWeb: {version['result']}")

        deck_names = post_request("deckNames")
        print(f"Existing decks: {deck_names['result']}")
        print("=" * 50)

    def create_cards(self, deck: str, content: dict[str], model: str = "Basic") -> None:
        """Create one (or several) cards based on the provided model.

        Args:
            deck (str): Deck.
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

        if new_card["Error"] is None:
            print("Card successfully created.")
        else:
            print(f"Error: {new_card['Error']}")
