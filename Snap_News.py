# https://www.marvelsnap.com/newslist

# https://marvelsnapzone.com/spotlight-caches/

import requests
import urllib
from urllib import request
from urllib.request import Request, urlopen

reponse = requests.get("https://marvelsnapzone.com/spotlight-caches/")
# print(reponse.text[20000:40000])

# u2 = urllib.request.urlopen('https://marvelsnapzone.com/spotlight-caches/')
req = Request(
    url='https://marvelsnapzone.com/spotlight-caches/',
    headers={'User-Agent': 'Mozilla/5.0'}
)
webpage = str(urlopen(req).read())
#print((str(webpage)).replace('\\n', '\n'))
cache_of_week = (webpage[webpage.index("Cache Week of"):webpage.index('"', webpage.index("Cache Week of"))])

coords_chr1 = [cache_of_week.index('Are', cache_of_week.index(':'))+3, cache_of_week.index(',', cache_of_week.index(':'))]
character_1 = cache_of_week[coords_chr1[0]:coords_chr1[1]]
coords_chr2 = [cache_of_week.index(',', cache_of_week.index(':'))+1, cache_of_week.index(" and ")-1]
character_2 = cache_of_week[coords_chr2[0]:coords_chr2[1]]
coords_chr3 = [cache_of_week.index(" and ")+4, cache_of_week.index(" Worth ")]
character_3 = cache_of_week[coords_chr3[0]:coords_chr3[1]]

img_chr1 = "https://static.marvelsnap.pro/cards/" + character_1.replace(" ", "").replace('.', '') + ".webp"
img_chr2 = "https://static.marvelsnap.pro/cards/" + character_2.replace(" ", "").replace('.', '') + ".webp"
img_chr3 = "https://static.marvelsnap.pro/cards/" + character_3.replace(" ", "").replace('.', '') + ".webp"

#print(character_1)

# for lines in webpage.readlines():
 # print(lines)