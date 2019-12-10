import os

from linebot import LineBotApi, WebhookParser
#from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

import requests 
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token,ImageSendMessage(
		original_content_url = text,
		preview_image_url = text
            )
    )
    return "OK"

def movie(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    print("movie")
    target_url = 'https://movies.yahoo.com.tw/'
    requests.packages.urllib3.disable_warnings()
    #rs = requests.session()
    res = requests.get(target_url, verify=False)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'html.parser')   
    content = ""
    for index, data in enumerate(soup.select('div.movielist_info h1 a')):
        if index == 20:
            return content       
        title = data.text
        link =  data['href']
        content += '{}\n{}\n'.format(title, link)

    line_bot_api.reply_message(reply_token,TextSendMessage(text=content))
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
