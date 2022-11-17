import requests
import json
import pprint

base_url='https://api.themoviedb.org/3'
url='/movie/top_rated'

query={
    'api_key':'625a9f192ec14bb97515a7d6900d2512',
    'language':'ko',
    'page':1,
}



total_res=[]
for i in range(1,2):
    query['page']=i
    response = requests.get(base_url+url,params=query).json()

    for movie in response['results']:
        for s in ["video","adult","original_language"]:
            movie.pop(s)
        d={
            "model":"movies.movie",
            "fields":movie
            }
        total_res.append(d)

pprint.pprint(total_res)
print(len(total_res))

with open('./movie_top20.json','w',encoding="utf-8") as f:
    json.dump(total_res,f,indent="\t", ensure_ascii=False)

