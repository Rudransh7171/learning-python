import requests
import json
c = str(input("similar word for?"))
b_url = 'https://api.datamuse.com/words'
d = {'rel_rhy':c}
req = requests.get(b_url,params=d)
x = req.json()
e = [d['word'] for d in x]
for i in e:
    print('->',i)
j = str(input('which word you like?'))
if j in e:
    print("Oh! Thast's cool")
else:
    print("Oops. That's not in list")
