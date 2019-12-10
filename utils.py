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

def send_video(reply_token, text_mp4, text_jpg):
    print("send")
    line_bot_api = LineBotApi(channel_access_token)
    message = VideoSendMessage(
        original_content_url = text_mp4,
        preview_image_url = text_jpg
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_templete_message(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/8lTsvo1.jpg',
            title='Menu',
            text='Please select',
            actions=[
                MessageTemplateAction(
                    label='picture',
                    text='貓貓照片'
                ),
                MessageTemplateAction(
                    label='video',
                    text='貓貓影片'
                ),
                URITemplateAction(
                    label='Meowed IG',
                    uri='https://www.instagram.com/meowed/?hl=zh-tw'
                )   
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"


def news(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)

    res = requests.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
    #Google國際新聞的網址
    soup = BeautifulSoup(res.text,"html.parser")
    content = ""
    count = 0
    for title,url in zip(soup.select("h4"),soup.select("h4 > a[href]")):
        if count < 10:
            #Google有時會換字體大小 像是h3改成現在的h4
            a = url['href'].replace("./", "")
            content += "{}\n'https://news.google.com/'{}\n".format(title.text, a)
        count += 1
    print(content)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=content))
    return "OK"

    
