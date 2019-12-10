import requests
from bs4 import BeautifulSoup
res = requests.get("https://news.google.com/topics/CAAqKggKIiRDQkFTRlFvSUwyMHZNRGx1YlY4U0JYcG9MVlJYR2dKVVZ5Z0FQAQ?hl=zh-TW&gl=TW&ceid=TW%3Azh-Hant")
#Google國際新聞的網址
soup = BeautifulSoup(res.text,"html.parser")
content = ""
count = 0
for title,url in zip(soup.select("h4"),soup.select("h4 > a[href]")):
    if count < 10:
        #Google有時會換字體大小 像是h3改成現在的h4

        a = url['href'].replace("./", "")
        a = 'https://news.google.com/'+a
        content += "{}\n{}\n".format(title.text, a)
    count += 1
print(content)