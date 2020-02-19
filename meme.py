from discord.message import File
from my_library import JSON
import os
import requests
import io
import urllib.parse


class Meme:

    @staticmethod
    def get_ext(url):
        return os.path.splitext(urllib.parse.urlparse(url).path)[-1]

    @staticmethod
    def download_meme(url):
        content = requests.get(url).content
        file = io.BytesIO(content)
        return file

    @staticmethod
    def getter(name):
        memes = JSON.read_json('memes.json')
        if name in memes:
            url = memes[name]
            file = Meme.download_meme(url)
            return File(file, filename=name + Meme.get_ext(url))
        else:
            return False
#CREATE CLEAR LIMIT FUNCTION
    @staticmethod
    def setter(name, url):
        JSON.add_json("memes.json", {name: url})

