from transitions.extensions import GraphMachine

#from utils import send_text_message, send_image
from utils import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_cat(self, event):
        text = event.message.text
        if text.lower() == "貓貓" or text.lower() == "貓咪" or text.lower() == "cat":
            return True
        else:
            return False
        #return text.lower() == "貓貓"

    def is_going_to_cat_picture(self, event):
        text = event.message.text
        return text.lower() == "貓貓照片"

    def is_going_to_cat_video(self, event):
        text = event.message.text
        return text.lower() == "貓貓影片"    

    def is_going_to_news(self, event):
        text = event.message.text
        return text.lower() == "新聞"

    def is_going_to_international(self, event):
        text = event.message.text
        return text.lower() == "國際"
    
    def is_going_to_business(self, event):
        text = event.message.text
        return text.lower() == "商業"

    def is_going_to_science(self, event):
        text = event.message.text
        return text.lower() == "科學與科技"

    def is_going_to_entertainment(self, event):
        text = event.message.text
        return text.lower() == "娛樂"
    
    def is_going_to_physical(self, event):
        text = event.message.text
        return text.lower() == "體育"

    def is_going_to_health(self, event):
        text = event.message.text
        return text.lower() == "健康"




    def on_enter_cat(self, event):
        print("I'm entering menu")
        reply_token = event.reply_token
        send_templete_message_cat(reply_token)
        #self.go_back()

    def on_exit_cat(self, event):
        print("Leaving menu")

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
        self.go_back()

    def on_exit_cat_video(self):
        print("Leaving state2")



    def on_enter_news(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_templete_message_news(reply_token)
        #news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW:zh-Hant")
        #send_text_message(reply_token, text)
        #self.go_back()

    def on_exit_news(self, event):
        print("Leaving state3")

    def on_enter_international(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_templete_message_news(reply_token)
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_international(self):
        print("Leaving state3")

    def on_enter_business(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_templete_message_news(reply_token)
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_business(self):
        print("Leaving state3")
    
    def on_enter_science(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_templete_message_news(reply_token)
        news(reply_token, "https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSkwyMHZNR1ptZHpWbUVnVjZhQzFVVnhvQ1ZGY29BQVAB?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_science(self):
        print("Leaving state3")

    def on_enter_entertainment(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_templete_message_news(reply_token)
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_entertainment(self):
        print("Leaving state3")

    def on_enter_physical(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_templete_message_news(reply_token)
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_physical(self):
        print("Leaving state3")

    def on_enter_health(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_templete_message_news(reply_token)
        news(reply_token, "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_health(self):
        print("Leaving state3")

