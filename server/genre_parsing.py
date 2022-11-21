import requests
import json
import pprint

base_url='https://api.themoviedb.org/3'
url='/genre/movie/list'

query={
    'api_key':'625a9f192ec14bb97515a7d6900d2512',
    'language':'ko',
}
response = requests.get(base_url+url,params=query).json()

genre_model=[]
for genre in response['genres']:
    d={
        'model':'movies.genre',
        'fields':genre
    }
    genre_model.append(d)

pprint.pprint(genre_model)
print(len(genre_model))

with open('./server/genres.json','w',encoding="utf-8") as f:
    json.dump(genre_model,f,indent="\t", ensure_ascii=False)

