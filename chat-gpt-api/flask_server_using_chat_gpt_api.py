import os
import json
from typing import List

import openai
from dotenv import load_dotenv
from flask import Flask, request

from flask_cors import CORS

from api_types import LLMResult
from prompts import *  # NOQA

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # default address of Next.js dev frontend


@app.route("/api/get-search-filter", methods=["POST"])
def search():
    text = request.args.get("text")
    query_object = interpret_text(text)
    return json.dumps(query_object)


def interpret_text(query: str) -> List[LLMResult]:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_MESSAGE},
            {"role": "user", "content": EXAMPLE_1_INPUT},
            {"role": "assistant", "content": EXAMPLE_1_OUTPUT},
            {"role": "user", "content": query},
        ],
    )
    llm_result = json.loads(response.choices[0].message.content)
    return llm_result


if __name__ == "__main__":
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    app.run(debug=True)
    # the endpoint /api/get-search-filter takes a holiday description in plain text and interprets it
    # as a json containing some fixed search filters using the openai API
    # see prompts.py for the example given to the LLM
    # example: $ curl --location --request POST 'http://127.0.0.1:5000/api/get-search-filter?text=I%20want%20to%20play%20tennis%20in%20france'
