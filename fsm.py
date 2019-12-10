from transitions.extensions import GraphMachine

#from utils import send_text_message, send_image
from utils import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_cat_picture(self, event):
        text = event.message.text
        '''if text.lower() == "貓貓照片":
            return True
        else:
            return False'''
        return text.lower() == "貓貓照片"

    def is_going_to_cat_video(self, event):
        text = event.message.text
        return text.lower() == "貓貓影片"

    def is_going_to_state3(self, event):
        text = event.message.text
        return text.lower() == "go to state3"

    def is_going_to_menu(self, event):
        text = event.message.text
        return text.lower() == "menu"

    def is_going_to_weather(self, event):
        text = event.message.text
        return text.lower() == "天氣"






    def on_enter_cat_picture(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_image(reply_token, "https://i.imgur.com/NinLHTp.jpg")
        self.go_back()

    def on_exit_cat_picture(self):
        print("Leaving state1")


    def on_enter_cat_video(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        send_video(reply_token, "https://i.imgur.com/Rq6m3PO.mp4", "https://i.imgur.com/haMAxrE.jpg")
        #self.go_back()

    def on_exit_cat_video(self, event):
        print("Leaving state2")


    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state3")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")


    def on_enter_menu(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_templete_message(reply_token)
        self.go_back()

    def on_exit_menu(self):
        print("Leaving menu")


    def on_enter_weather(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW:zh-Hant")
        #send_text_message(reply_token, text)
        self.go_back()

    def on_exit_weather(self):
        print("Leaving state3")

