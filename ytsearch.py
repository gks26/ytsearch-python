import os
import requests


class Youtube:
    def __init__(self, api_key):
        self.__api_key__ = api_key
        self.__endpoint__ = "https://www.googleapis.com/youtube/v3/"
        if self.__api_key__ == None:
            self.__api_key__ = ""

    def set_api_key(self, key):
        self.__api_key__ = key

    def get_api_key(self):
        return self.__api_key__

    def make_request(self, url, param:dict):
        param_str = "?"
        for key in param.keys():
            param_str+=f"{key}={param[key]}&"
        response = requests.get(self.__endpoint__+url+param_str)
        return response

    def search(self, query, maxresult):
        param = {"part":"snippet", "key":self.__api_key__, "q":query, "maxresult":maxresult}
        response_json = self.make_request('search', param).json()
        items = response_json['items']
        result  = [item['snippet'] for item in items]
        for i, v in enumerate(items):
            result[i]['url'] = f"https://youtube.com/watch?v={v['id']['videoId']}"
        return result