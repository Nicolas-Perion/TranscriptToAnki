from to_json_schema.to_json_schema import SchemaBuilder
import json

from ollama import chat

from config import MODEL, SYSTEM_PROMPT, SESSION_PROMPT


schema_builder = SchemaBuilder()

TOTAL_PROMPT = "\n".join([SYSTEM_PROMPT, SESSION_PROMPT])


class BasicSchema:
    def schema(self) -> dict[str, str]:
        return {"Front": "string", "Back": "string"}


class CardsBundle:
    def __init__(self, cards_amount: int) -> None:
        self.cards_amount = cards_amount
        self.basic_schema = BasicSchema()

    def schema(self) -> dict:
        return {
            f"Card {i}": self.basic_schema.schema() for i in range(self.cards_amount)
        }


def write_cards_content(
    transcription_path: str, bundle_size: int
) -> dict[str, dict[str, str]]:
    """Generate the content of a card based on a transcription.

    Args:
        transcription (str): The transcription to generate content from.

    Returns:
        str: The generated content, formated by the schema.
    """

    bundle = CardsBundle(bundle_size)
    schema = schema_builder.to_json_schema(bundle.schema())

    with open(transcription_path, encoding="utf-8") as file:
        response = chat(
            model=MODEL,
            format=schema,
            messages=[
                {"role": "system", "content": TOTAL_PROMPT},
                {
                    "role": "user",
                    "content": f"Here is the information about the topic: <information> {''.join(file.readlines())} </information>",
                },
            ],
        )

    return json.loads(response.message.content)
