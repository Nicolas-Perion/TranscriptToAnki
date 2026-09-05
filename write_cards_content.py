from ollama import chat
from pydantic import BaseModel

from config import MODEL

SYSTEM_PROMPT = """
You are an Anki card creator.
You will receive information about a topic and must generate content for the fields
of the card (Front, Back) and be compliant with the provided JSON schema.
The 'Front' field must contain one short question (at most 10 words) and the 'Back'
field must contain the answer to that question. 
"""


class CardFields(BaseModel):
    Front: str
    Back: str
    # tags: list[str]


schema = CardFields.model_json_schema()


def write_cards_content(transcription_path: str) -> str:
    """Generate the content of a card based on a transcription.

    Args:
        transcription (str): The transcription to generate content from.

    Returns:
        str: The generated content, formated by the schema.
    """
    with open(transcription_path) as file:
        response = chat(
            model=MODEL,
            format=schema,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {
                    "role": "user",
                    "content": rf"Here is the information about the topic: <\information> {file.readlines()} <\information>",
                },
            ],
        )

    return response.message.content
