import requests
from pprint import pprint
from dotenv import load_dotenv
import os 

# load .env
load_dotenv()


def recommendation(title):
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
    path2 = f'/movie/{re_id}/recommendations'
    response2 = requests.get(BASE_URL+path2, params=params).json()
    result2 = response2['results']
    li = []
    for i in result2:
        li.append(i['title'])
    return li
    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
