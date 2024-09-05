import requests
import urllib
from urllib import request
from urllib.request import Request, urlopen


reponse = requests.get("https://marvelsnapzone.com/spotlight-caches/")
print(reponse)


#print(card_effect)

def get_card_effect(character):
    req = Request(
        url='https://marvelsnapzone.com/cards/' + character.replace('.', '-').replace(' ', '-') + '/',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = str(urlopen(req).read())
    card_effect = (webpage[webpage.index("ability:") + 9:webpage.index('.', webpage.index("ability:")) + 1])
    return card_effect

