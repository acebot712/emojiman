import os
import openai
from dotenv import load_dotenv
import urllib.parse

load_dotenv()  # take environment variables from .env.

openai.api_key = os.getenv("OPENAI_API_KEY")


def handle_request(request):
    movie = urllib.parse.unquote(request)
    movie = movie.title() + ": "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Convert movie titles into emoji.\n\nBack to the Future: 👨👴🚗🕒 \nBatman: 🤵🦇 \nTransformers: 🚗🤖 \n{movie}",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"],
    )
    return response.choices[0].text


if __name__ == "__main__":
    print("Response")
    # print(response.choices[0].text)
