#!/usr/bin/env python
"""Create a deck with the deck of cards api,
deal 4 cards in a number of players
and list the players hands"""

import requests
import sys
import json

base_url = "https://deckofcardsapi.com/api/deck/"
qstr = {"count":"4"}
hdr = {
    'Cache-Control': "no-cache",
    }

def dealcards(deck_id,playername):
    action="/draw/"
    full_url = base_url+deck_id+action
    response = requests.request("GET", full_url, headers=hdr, params=qstr)
    drawncards = json.loads(response.text)["cards"]
    codes = []
    for card in drawncards:
        codes.append(card["code"])
    joinstring = ","
    codelist = joinstring.join(codes)
    action="/add/?cards="
    full_url = base_url+deck_id+"/pile/"+playername+action+codelist
    #create a card pile for player with drawn cards
    response = requests.request("GET", full_url, headers=hdr, params=qstr)
    return json.loads(response.text)["success"]

def main():
    deck_id=input("what is the deck_id? ")
    players=input("how many players (1-5)?")
    for i in range(1,int(players)+1):
        pile_name="player"+str(i)
        #draw five cards for player and put them in his pile
        result = dealcards(deck_id,pile_name)
        full_url = base_url+deck_id+"/pile/"+pile_name+"/list/"
        #list player's cards
        resp = requests.request("GET", full_url,
                                    headers=hdr, params=qstr)
        plcards = json.loads(resp.text)["piles"][pile_name]["cards"]
        print(pile_name,"cards:")
        for card in plcards:
            print(card["code"])

if __name__ == '__main__':
    sys.exit(main())
