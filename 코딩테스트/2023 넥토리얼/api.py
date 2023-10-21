import math
import os
import random
import re
import sys
import requests


def bestInGenre(genre):
    baseUrl = "https://jsonmock.hackerrank.com/api/tvseries?page="
    info = []
    for page in range(1, 21):
        requestUrl = baseUrl + str(page)

        # GET 요청 보내기
        response = requests.get(requestUrl)

        # 응답 확인
        if response.status_code != 200:
            return
        response = response.json()
        for series in response["data"]:
            if genre in series["genre"]:
                info.append((series["name"], series["imdb_rating"]))
    info.sort(key=lambda x: (-x[1], x[0]))
    return info[0][0]

print(bestInGenre('Action'))