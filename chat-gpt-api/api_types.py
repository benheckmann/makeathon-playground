from typing import TypedDict


class LLMResult(TypedDict):
    """This result will be directly returned from the LLM."""

    destination: str
    origin: str
    departure_date: str
    return_date: str
    count_adults: int
    count_children: int
    explanation: str
