import sys
import requests

def get_data(pokemon_name):
    api = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(api)

    if response.status_code!=200:
        print(f"No pokemon by name '{pokemon_name}'.")
        sys.exit(1)

    return response.json()

def download_sprite(sprite_url):
    response=requests.get(sprite_url)
    if response.status_code==200:
        with open('sprite.png','wb') as file:
            file.write(response.content)

    else :
        print(" No pokemon sprite found.")

def main():
    if len(sys.argv)!=2:
        print(" arg must be of form python pokemon_api.py 'pokemon_name'.")
        sys.exit(1)

    pokemon_name=sys.argv[1]
    data=get_data(  pokemon_name)

    print(f"Name:{pokemon_name.capitalize()}")
    print(f"National number: {data['id']}")
    print(f"Height: {data['height']/10}")
    print(f"Weight : {data['weight']/10}")
    abilities=[]
    for ability in data['abilities']:
        abilities.append(ability['ability']['name'])


    types=[]
    for type in data['types']:
        types.append(type['type']['name'])


    base_stats = {}
    for stat in data['stats']:
        base_stats[stat['stat']['name']] = stat['base_stat']

    
    print(f"Abilities: {', '.join(abilities)}")
    print(f"Types: {', '.join(types)}")
    print("Base stats:")
    for stat, value in base_stats.items():
        print(f" {stat}: {value}")
        



    download_sprite(data['sprites']['other']['official-artwork']['front_default'])   
    print(" Sprite downloaded as 'sprite.png'.")                 


if __name__=="__main__":
    main()    