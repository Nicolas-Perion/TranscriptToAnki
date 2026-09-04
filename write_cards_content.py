from ollama import chat
from pydantic import BaseModel

from config import MODEL

SYSTEM_PROMPT = """
You are an Anki card creator.
You will receive information about a topic and must generate content for the fields of
of the card (Front, Back, tags) and be compliant with the provided JSON schema.
"""


class CardFields(BaseModel):
    Front: str
    Back: str
    tags: list[str]


schema = CardFields.model_json_schema()


def write_cards_content(transcription: str):

    response = chat(
        model=MODEL,
        think="low",
        format=schema,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {
                "role": "user",
                "content": rf"Here is the information: <\information> {transcription} <\information>",
            },
        ],
    )

    return print(response.message.content)
