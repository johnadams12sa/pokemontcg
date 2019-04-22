from pokemontcgsdk import Card
from pokemontcgsdk import Set
from pokemontcgsdk import Type
from pokemontcgsdk import Supertype
from pokemontcgsdk import Subtype
#from pokemontcgsdk import requests

#create variable to get user input
usr_input = input('Search Pokemon Name ')

#api request through this link https://api.pokemontcg.io/v1/cards?name=usr_input

#create request object for API call
#req = requests.get("https://api.pokemontcg.io/v1/cards?name=%s" % usr_input)
#req.json()