import requests
from pprint import pprint
from dotenv import load_dotenv
import os 

# load .env
load_dotenv()


def credits(title):
    pass
    # 여기에 코드를 작성합니다.
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': os.environ.get('apikey'),
    'language': 'ko-KR',
    'region': 'KR',
    'query' : title
    }
    response = requests.get(BASE_URL+path, params=params).json()
    result = response['results']
    try:
        re_id = result[0]['id']
    except:
        return None
    path2 = f'/movie/{re_id}/credits'
    response2 = requests.get(BASE_URL+path2, params=params).json()
    cast = response2['cast']
    crew = response2['crew']
    li_cast = []
    li_crew = []
    di = {'cast': li_cast, 'crew' : li_crew}
    for i in cast:
        if i['cast_id'] <= 10:
            li_cast.append(i['name'])
    for j in crew:
        if j['known_for_department'] == 'Directing' and j['name'] not in li_crew:
            li_crew.append(j['name'])
    return di

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록 반환
    영화 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
