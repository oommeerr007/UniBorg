from telethon import events, utils
from telethon.tl import types, functions

import html
import urllib.request

import re
import os
import asyncio
import random
import json
from urllib.request import urlopen, urlretrieve
from urllib.parse import quote_plus, urlencode
import requests

from uniborg.util import admin_cmd


@borg.on(admin_cmd("boob ?(.*)"))
async def boobs(boo):
    nsfw = requests.get('http://api.oboobs.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'booob.jpg')
    await borg.send_file(boo.chat_id, "booob.jpg")
    
    
@borg.on(admin_cmd("butt ?(.*)"))
async def butts(but):
    nsfw = requests.get('http://api.obutts.ru/noise/1').json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), "*.jpg")
    os.rename('*.jpg', 'buttt.jpg')
    await borg.send_file(but.chat_id, "buttt.jpg")