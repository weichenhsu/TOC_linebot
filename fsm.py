from transitions.extensions import GraphMachine

#from utils import send_text_message, send_image
from utils import *

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_state1(self, event):
        print("go to state1 ing")
        text = event.message.text
        '''if text.lower() == "go to state1":
            return True
        else:
            return False'''
        return text.lower() == "go to state1"

    def is_going_to_state2(self, event):
        print("go to state2 ing")
        text = event.message.text
        return text.lower() == "go to state2"

    def is_going_to_state3(self, event):
        print("go to state3 ing")
        text = event.message.text
        return text.lower() == "go to state3"

    def on_enter_state1(self, event):
        print("I'm entering state1")

        reply_token = event.reply_token
        send_text_message(reply_token, "Trigger state1")
        self.go_back()

    def on_exit_state1(self):
        print("Leaving state1")

    def on_enter_state2(self, event):
        print("I'm entering state2")

        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state2")
        movie(reply_token)
        self.go_back()

    def on_exit_state2(self):
        print("Leaving state2")

    def on_enter_state3(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        #send_text_message(reply_token, "Trigger state3")
        send_image(reply_token, "https://lh3.googleusercontent.com/EezBy27SQdmve_agfLLNjXoVcYb3jpvc-tbTGHTWNuKhERs2Ksrzoc0Yo0lAA3Nt7PQWCckynys9lDx3IQ-Csad9iIrRHHAHZg17XQEE4rh9Jfrko04iJJTyLx6W1AK7DUWfcKfNR7Xbg9-Zg1Yu0UxqVtrimkaDc0f3XIv050hxxkroUg4LKU5wAiS08XAhgtyRQfxO9qd-io6andbcNxEke8YS_dLqb-mup9CQZNQ8lq5iC5YX2WwHKhICcnnAFrTsqmYbgf9cCESTvHx52JUhsNVlHex-OqU5EcEhzWcCtuRthFSgk6ehdExLR07LrCC1z80fqfmGH2dxzTzbsOmIBNe7ENvKNSxiQv_lD3xC3xA8s19yki6FRKnOfmg1THxgTW8RpcXZaXld-ElEjEs_YSh5pKJkzu1uUbIErMsh6VkxUt5AWw7rOWexs4_L76qNcZpZUV1ZB6XRFvOt0id44isFPnUsNaFZJF50IzCYv0Sr8X0NBPQ9Eye9uXhvAWTiX53wgqIzTKbTflvl2rXF1pxrNnkAH0YYJso6xp70rArH4oICEx7JwS1DeWQAqMt2GyoW3LnbWa94sD9qdn9ik3Kc5LZZVwNJUQrkHgZt99usfLYn5VD1_a0lWnYu6ZKPgrNsXKjDRf0cd7Mo5F4UwxEUJTfy2qEQrYuKXk-Ed4uRgmkvwB0=w534-h949-no")
        self.go_back()

    def on_exit_state3(self):
        print("Leaving state3")

