from curses.ascii import isalpha
from typing import Union
from fastapi import FastAPI
from starlette.responses import RedirectResponse
import random

app = FastAPI()

@app.get('/')
def redirect_to_docs():
    response = RedirectResponse(url='/docs')
    return response

@app.get('/anger-translator/{message}')
def get_anger_translator_message(message: str):
    if not message:
        return message

    return __create_angry_message(message)

@app.get('/sponge-mock/{message}')
def get_sponge_mock_message(message: str):
    if not message:
        return message

    return __create_mock_message(message)

def __create_mock_message(message: str):
    result = ''
    for ch in message:
        if ch.isalpha():
            random_num = random.random()
            result += ch.upper() if random_num > 0.5 else ch.lower()
        else:
            result += ch
    return result


def __create_angry_message(message: str):
    message = [__add_clap_emoji(x) for x in message.split()]
    return '👏 ' + ''.join(message).strip()

def __add_clap_emoji(word: str):
    return f'{word.upper()} 👏 '
