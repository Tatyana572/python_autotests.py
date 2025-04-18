import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'token'
HEADER = {'Content-Type': 'application/json', 'trainer_token' :TOKEN}

body_create = {
    "name": "Коржик",
    "photo_id": 3
}

respons_create = requests.post(url=f'{URL}/pokemons', headers= HEADER, json= body_create)
print(respons_create.text)

pokemon_id =respons_create.json()["id"] 

body_new = {
    "pokemon_id": pokemon_id,
    "name": "JSON",
    "photo_id": 2
}
respons_create = requests.put(url=f'{URL}/pokemons', headers= HEADER, json=body_new )
print(respons_create.text)

body_pokeball = {
    "pokemon_id": pokemon_id
}
respons_pokeball = requests.post(url=f'{URL}/trainers/add_pokeball', headers= HEADER, json=body_pokeball)
print(respons_pokeball.text)