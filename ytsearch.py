import os
import requests

class Youtube:
    def __init__(self, api_key):
        self.__api_key__ = api_key
        self.__endpoint__ = "https://www.googleapis.com/youtube/v3/"

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

    def search(self, type, query, maxresult):
        if type not in ['video', 'channel', 'playlist']:
            raise ValueError("Invalid filter parameter. Must be 'channel', 'video', or 'playlist'.")
        if type == "video":
            resource_url = "https://youtube.com/watch?v="
        elif type == "channel":
            resource_url = "https://youtube.com/channel/"
        elif type == "playlist":
            resource_url = "https://youtube.com/playlist"
        param = {"part":"snippet", "key":self.__api_key__, "type":type, "q":query, "maxResults":maxresult}
        response_json = self.make_request('search', param).json()
        items = response_json['items']
        result  = [item['snippet'] for item in items]
        for i, v in enumerate(items):
            id = v['id']
            if type == "video":
                result[i]['url'] = resource_url+id['videoId']
            elif type == "channel":
                result[i]['url'] = resource_url+id['channelId']
            elif type == "playlist":
                result[i]['url'] = resource_url+id['playlistId']
        return result