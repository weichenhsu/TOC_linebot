# TOC Project 2020
## 前言
每次在翻找相簿時，都有許多其他照片，使得瀏覽起來相對困難，想整理一個地方存放貓咪的照片，想看就可以看到。
我自己比較懶得去新聞網站上面找新聞看，大多看到的都是社群網站上的娛樂新聞較多，想做個新聞搜尋，讓自己可以輕易地找到想看的分類的新聞。



## Finite State Machine
![fsm](https://i.imgur.com/3VagzQo.png)

## Usage
The initial state is set to `user`.

There are two branches - `cat` and `news`. It can jump to another branch.

In the`cat` state, user can get picture or video of cat. User can go to Instagram account of MEOWED.

In the `news` state, user has six different categories of news to choose. Then, Line bot will return four popular news in the category.

ALL INPUT are case-insensitive.

- State:`user`
	- Input:"cat" or "貓咪" or "貓貓"
		- State:`cat`
		- Reply:`cat`功能選單
		    - Input:"貓咪圖片" or "cat picture" or "picture"
		        - State:`cat_picture`
		        - Reply: 隨機貓咪照片一張
		        - Return:`user`
		    - Input:"貓咪影片" or "cat video" or "video"
		        - State:`cat_video`
		        - Reply:隨機貓咪影片一則
		        - Return:`user`
		    - Input:"新聞" or "News"
		        - State:`news`

	- Input: "news" or "新聞"
		- State:`news`
		- Reply:`news`功能選單
		    - Input:"國際" or "International"
		        - State:`international`
		        - Reply:四則熱門國際新聞
		        - Return:`user`
		    - Input:"商業" or "business"
		        - State:`business`
		        - Reply:四則熱門商業新聞
		        - Return:`user`
		    - Input:"科學與科技" or "科學" or "科技" or "science"
		        - State:`science`
		        - Reply:四則熱門科學與科技新聞
		        - Return:`user`
		    - Input:"娛樂" or "entertainment"
		        - State:`entertainment`
		        - Reply:四則熱門娛樂新聞
		        - Return:`user`
            - Input:"體育" or "physical"
		        - State:`physical`
		        - Reply:四則熱門體育新聞
		        - Return:`user`
		    - Input:"健康" or "health"
		        - State:`health`
		        - Reply:四則熱門健康新聞
		        - Return:`user`
		    - Input:"cat" or "貓咪" or "貓貓"
		        - State:`cat`

## Demo
### Cat State
![](https://i.imgur.com/j5D1swp.jpg)
![](https://i.imgur.com/yy9WgjT.jpg)
![](https://i.imgur.com/UXTCCRN.jpg)
### News State
![](https://i.imgur.com/hyJdyJy.jpg)
![](https://i.imgur.com/NcEHlII.jpg)