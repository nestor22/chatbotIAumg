import json
import difflib
from difflib import get_close_matches

data = {
    'parciales': 'para la seccion b 3 y 4',
    'inscripcion': 'para la seccion b 3 y 4',
}

def translate(word):
    word = str(word)
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys()))>0:
        return data[get_close_matches(word, data.title())[0]]
    else:
        return "No tengo informacion al respecto dejame contactar con un humano."
