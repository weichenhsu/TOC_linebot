from transitions.extensions import GraphMachine
from utils import *
import random

picture = ["https://imgur.com/JL1zwCv.jpg",
            "https://imgur.com/8lTsvo1.jpg",
            "https://imgur.com/ONdJRvL.jpg",
            "https://imgur.com/haMAxrE.jpg",
            "https://imgur.com/Yu33342.jpg",
            "https://imgur.com/NinLHTp.jpg",
            "https://imgur.com/gzO6lIo.jpg",
            "https://imgur.com/utxw1y7.jpg",
            "https://imgur.com/2aQRaJO.jpg",
            "https://imgur.com/YlxSZAB.jpg",
            "https://imgur.com/g6OXNpf.jpg",
            "https://imgur.com/n6n6QAb.jpg"
            ]




class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_cat(self, event):
        text = event.message.text
        if text.lower() == "貓貓" or text.lower() == "貓咪" or text.lower() == "cat":
            return True
        else:
            return False

    def is_going_to_cat_picture(self, event):
        text = event.message.text
        if text.lower() == "貓貓照片" or text.lower() == "貓咪照片" or text.lower() == "cat picture" or text.lower() == "照片" or text.lower() == "picture":
            return True
        else:
            return False

    def is_going_to_cat_video(self, event):
        text = event.message.text
        if text.lower() == "貓貓影片" or text.lower() == "貓咪影片" or text.lower() == "cat video" or text.lower() == "影片" or text.lower() == "video":
            return True
        else:
            return False  

    def is_going_to_news(self, event):
        text = event.message.text
        if text.lower() == "新聞" or text.lower() == "news":
            return True
        else:
            return False

    def is_going_to_international(self, event):
        text = event.message.text
        if text.lower() == "國際" or text.lower() == "international":
            return True
        else:
            return False
    
    def is_going_to_business(self, event):
        text = event.message.text
        if text.lower() == "商業" or text.lower() == "business":
            return True
        else:
            return False

    def is_going_to_science(self, event):
        text = event.message.text
        if text.lower() == "科學與科技" or text.lower() == "science" or text.lower() == "科學" or text.lower() == "科技":
            return True
        else:
            return False

    def is_going_to_entertainment(self, event):
        text = event.message.text
        if text.lower() == "娛樂" or text.lower() == "entertainment":
            return True
        else:
            return False
    
    def is_going_to_physical(self, event):
        text = event.message.text
        if text.lower() == "體育" or text.lower() == "physical":
            return True
        else:
            return False

    def is_going_to_health(self, event):
        text = event.message.text
        if text.lower() == "健康" or text.lower() == "health":
            return True
        else:
            return False



    def on_enter_cat(self, event):
        reply_token = event.reply_token
        send_templete_message_cat(reply_token)
        #self.go_back()

    def on_exit_cat(self, event):
        print("Leaving cat menu")

    def on_enter_cat_picture(self, event):
        reply_token = event.reply_token
        i = random.randint(0, len(picture) -1)
        send_image(reply_token, picture[i])
        #send_image(reply_token, "https://i.imgur.com/NinLHTp.jpg")
        self.go_back()

    def on_exit_cat_picture(self):
        print("Leaving cat_picture")


    def on_enter_cat_video(self, event):
        reply_token = event.reply_token
        send_video(reply_token, "https://i.imgur.com/Rq6m3PO.mp4", "https://i.imgur.com/haMAxrE.jpg")
        self.go_back()

    def on_exit_cat_video(self):
        print("Leaving cat_video")



    def on_enter_news(self, event):
        reply_token = event.reply_token
        send_templete_message_news(reply_token)
        #self.go_back()

    def on_exit_news(self, event):
        print("Leaving news menu")

    def on_enter_international(self, event):
        reply_token = event.reply_token
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_international(self):
        print("Leaving international")

    def on_enter_business(self, event):
        reply_token = event.reply_token
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx6TVdZU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_business(self):
        print("Leaving business")
    
    def on_enter_science(self, event):
        reply_token = event.reply_token
        news(reply_token, "https://news.google.com/topics/CAAqLAgKIiZDQkFTRmdvSkwyMHZNR1ptZHpWbUVnVjZhQzFVVnhvQ1ZGY29BQVAB?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_science(self):
        print("Leaving science")

    def on_enter_entertainment(self, event):
        reply_token = event.reply_token
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNREpxYW5RU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_entertainment(self):
        print("Leaving entertainment")

    def on_enter_physical(self, event):
        reply_token = event.reply_token
        news(reply_token, "https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRFp1ZEdvU0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_physical(self):
        print("Leaving physical")

    def on_enter_health(self, event):
        reply_token = event.reply_token
        news(reply_token, "https://news.google.com/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JYcG9MVlJYS0FBUAE?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
        self.go_back()

    def on_exit_health(self):
        print("Leaving health")

