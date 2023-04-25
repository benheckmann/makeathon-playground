# note: according to the gpt-3.5 docs, the system message tends to be ignored; writing the instruction in a user message is generally safer
SYSTEM_MESSAGE = """You are an assistant that interprets a short holiday description and returns a JSON object from that. The JSON object has the following fields:

- destination: str (the holiday destination)
- origin: str (the location of departure)
- departure_date: str (timestamp of the departure date)
- return_date: str (timestamp of the return date)
- count_adults: int (number of adults)
- count_children: int (number of children)
- explanation: str (a short explanation of one or two sentences justifying your destination or other parameters)

Choose meaningful values for all fields that cannot be interpreted from the input. The current year is 2023. The origin (if not specified otherwise) is Munich, Germany."""

EXAMPLE_1_INPUT = "I want to go skiing with my family in january"

EXAMPLE_1_OUTPUT = """{
    "destination": "Zermatt, Switzerland",
    "origin": "Munich, Germany",
    "departure_date": "2024-01-01",
    "return_date": "2024-01-08",
    "count_adults": 2,
    "count_children": 2,
    "explanation": "Zermatt is one of the most famous ski resorts in Europe, known for its breathtaking views of the Matterhorn, charming village atmosphere and extensive ski slopes. With over 360 kilometers of pistes and a high-altitude ski area up to 3,883 meters, Zermatt offers guaranteed snow, varied terrain for all skill levels and numerous off-piste opportunities. In addition, the resort is car-free, ensuring a peaceful and clean environment in which to enjoy your vacation."
}"""
