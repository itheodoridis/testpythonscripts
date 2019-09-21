import requests
import json

url = "https://deckofcardsapi.com/api/deck/new/shuffle/"
parameters = {"deck_count":"1"}

headers = {
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, headers=headers, params=parameters)

print(response.text)
deck_id=json.loads(response.text)["deck_id"]
print(deck_id)
