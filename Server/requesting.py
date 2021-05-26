import requests
import json

path = "./movies/fixtures/movies.json"
API_KEY = 'f4e4ad237c7fb44ea8e4abb88193fa30'

movies = []


# 500page까지만 요청 가능(10000개 데이터) 1page~500page
for i in range(1, 30):
    URL = (f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page={i}')
    response = requests.get(URL)
    data = response.json()
    # print(data)
    for j in range(20):

        adult = data.get('results')[j].get('adult')
        id = (i-1) * 20 + j + 1
        # genre_ids = data.get('results')[j].get('genre_ids')
        movie_id = data.get('results')[j].get('id')
        original_language = data.get('results')[j].get('original_language')
        original_title = data.get('results')[j].get('original_title')
        overview = data.get('results')[j].get('overview')
        popularity = data.get('results')[j].get('popularity')
        poster_path = data.get('results')[j].get('poster_path')
        release_date = data.get('results')[j].get('release_date')
        title = data.get('results')[j].get('title')
        vote_average = data.get('results')[j].get('vote_average')
        vote_count = data.get('results')[j].get('vote_count')
        temp_dict = {
            'adult': adult,
            'id': id,
            # 'genre_ids': genre_ids,
            'movie_id': movie_id,
            'original_language': original_language,
            'original_title':  original_title,
            'overview': overview,
            'popularity': popularity,
            'poster_path': poster_path,
            'release_date': release_date,
            'title': title,
            'vote_average': vote_average,
            'vote_count': vote_count,
            # 'recommend': [],
        }
        RECOMMEND_URL = (f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key={API_KEY}&language=ko-KR')
        recommend_response = requests.get(RECOMMEND_URL)
        recommend_data = recommend_response.json()
        try:
            for j in range(3):
                # temp_dict['recommend'].append(recommend_data.get('results')[j].get('title'))
                recommend_id = recommend_data.get('results')[j].get('id')
                KEYWORD_URL = (f'https://api.themoviedb.org/3/movie/{recommend_id}/keywords?api_key={API_KEY}')
                keyword_response = requests.get(KEYWORD_URL)
                keyword_data = keyword_response.json().get('keywords')
                # print(len(keyword_data))
                # print(keyword_data[0])
                for k in range(len(keyword_data)):
                    # print(keyword_data[k].get('id'), keyword_data[k].get('name'))
                    if keyword_data[k].get('id') == 818:
                        if keyword_data[0].get('id') == 818:
                            temp_dict['recommend'] = keyword_data[1].get('name')
                        else:
                            temp_dict['recommend'] = keyword_data[0].get('name')
        except:
            continue
        

        if temp_dict.get('recommend'):
            original_title = temp_dict.get('title')
            original_title = original_title.replace(' ', '')
            # print(original_title)
            BOOK_URL = (f'http://book.interpark.com/api/search.api?key=0CA17E2093AF4A55305F3AB7ECAA6A16517D8B64D9B9630B9A8D010573B88FE0&query={original_title}&output=json')
            BOOK_RESPONSE = requests.get(BOOK_URL)
            # &searchTarget=foreign
            Book_data = BOOK_RESPONSE.json()
            # print(Book_data)
            # print(Book_data.get('link'))
            # print('------------------------------')
            if Book_data.get('item'):
                # print(original_title)
                # print(Book_data.get('item')[0].get('link'))
                # print(Book_data.get('item')[0].get('title'))
                book_link = Book_data.get('item')[0].get('link')
                book_title = Book_data.get('item')[0].get('title')
                temp_dict['book_link'] = book_link
                temp_dict['book_title'] = book_title

                # {
                #     'book_link': book_link,
                #     'book_title': book_title,
                # }

                movie = {}
                movie["model"] = "movies.Movie"
                movie["pk"] = temp_dict.get('id')
                movie['fields'] = {}
                flag = 0
                for key, value in temp_dict.items():
                    if key == 'id':
                        continue
                    else:
                        movie['fields'][key] = value
                movies.append(movie)
   

with open(path, 'w', encoding='UTF-8') as outfile:
    json.dump(movies, outfile, indent="\t", ensure_ascii=False)

