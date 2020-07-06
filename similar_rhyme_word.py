import requests
import json

c = str(input("similar word for?"))
b_url = 'https://api.datamuse.com/words'
d = {'rel_rhy':c}
req = requests.get(b_url,params=d)
x = req.json()
print([d['word'] for d in x])
