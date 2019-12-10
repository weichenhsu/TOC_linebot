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

def send_video(reply_token, text):
    print("send")
    line_bot_api = LineBotApi(channel_access_token)
    message = VideoSendMessage(
        original_content_url = text,
        preview_image_url = text
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_templete_message(reply_token):
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/8lTsvo1.jpg',
            title='Menu',
            text='Please select',
            actions=[
                PostbackTemplateAction(
                    label='postback',
                    text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageTemplateAction(
                    label='message',
                    text='test'
                ),
                URITemplateAction(
                    label='uri',
                    uri='https://i.imgur.com/TgmgaPf.mp4'
                )   
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)


def movie(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    print("movie")

    r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html") #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser
    sel = soup.select("span.tem-C is-active") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
    content = ""
    for s in sel:
        print(s["href"], s.text) 
        content += s.text


    '''
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
        content += '{}\n{}\n'.format(title, link)'''

    line_bot_api.reply_message(reply_token,TextSendMessage(text=content))
    return "OK"


"""
def send_image_url(id, img_url):
    pass

def send_button_message(id, text, buttons):
    pass
"""
