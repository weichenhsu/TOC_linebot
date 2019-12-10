import os

from linebot import LineBotApi, WebhookParser
#from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import *

import requests
from bs4 import BeautifulSoup

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

def send_templete_message_cat(reply_token):
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

def send_templete_message_news(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            thumbnail_image_url='https://i.imgur.com/rETMF3V.jpg',
            title='News',
            text='Please select',
            actions=[
                MessageTemplateAction(
                    label='國際',
                    text='國際'
                ),
                MessageTemplateAction(
                    label='商業',
                    text='商業'
                ),
                MessageTemplateAction(
                    label='科學與科技',
                    text='科學與科技'
                ),
                MessageTemplateAction(
                    label='娛樂',
                    text='娛樂'
                ),
                MessageTemplateAction(
                    label='體育',
                    text='體育'
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"



def news(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)

    res = requests.get(url)
    soup = BeautifulSoup(res.text,"html.parser")
    content = ""
    count = 0
    for title,url in zip(soup.select("h4"),soup.select("h4 > a[href]")):
        if count < 5:
        #Google有時會換字體大小 像是h3改成現在的h4

            a = url['href'].replace("./", "")
            a = 'https://news.google.com/'+a
            content += "{}\n{}\n".format(title.text, a)
        count += 1
    #print(content)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=content))

    return content

    
''',
                MessageTemplateAction(
                    label='娛樂',
                    text='娛樂'
                ),
                MessageTemplateAction(
                    label='體育',
                    text='體育'
                ),
                MessageTemplateAction(
                    label='健康',
                    text='健康'
                )'''