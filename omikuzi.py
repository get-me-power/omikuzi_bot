# -*- encoding: utf-8 -*-
from numpy.random import *
import json
import twitter
import requests
from requests_oauthlib import OAuth1Session

CK = 'xxxxxxxxxxxxx'                            # Consumer Key
CS = 'xxxxxxxxxxxxx'   # Consumer Secret
AT = 'xxxxxxxxxxxxx'	# Access Token
AS = 'xxxxxxxxxxxxx'        # Accesss Token Secert

auth = twitter.OAuth(consumer_key="xxxxxxxxxxxxx",
    consumer_secret="xxxxxxxxxxxxx",
    token="xxxxxxxxxxxxx",
    token_secret="xxxxxxxxxxxxx")

url_media = "https://upload.twitter.com/1.1/media/upload.json"
url_text = "https://api.twitter.com/1.1/statuses/update.json"

# OAuth認証 セッションを開始
auth2 = OAuth1Session(CK, CS, AT, AS)

t_userstream = twitter.TwitterStream(auth=auth,domain='userstream.twitter.com')

for msg in t_userstream.user():

	if('text' in msg.keys() and msg['text']=='おみくじ'):

		number = randint(1,15)

		if number == 1:
			# 画像投稿
			files = {"media" : open('omikuzi_kuronuri.jpg', 'rb')}

		elif number == 2:
			files = {"media" : open('omikuzi_kiti.JPG', 'rb')}

		elif number == 3:
			files = {"media" : open('omikuzi_daikiti.JPG', 'rb')}

		elif number == 4:
			files = {"media" : open('omikuzi_kyo.JPG', 'rb')}

		elif number == 5:
			files = {"media" : open('omikuzi_kyo2.JPG', 'rb')}

		elif number == 6:
			files = {"media" : open('omikuzi_kyo3.JPG', 'rb')}

		elif number == 7:
			files = {"media" : open('fu*k.jpg', 'rb')}

		elif number == 8:
			files = {"media" : open('omikuzi_daikyo.JPG', 'rb')}

		elif number == 9:
			files = {"media" : open('omikuzi_daikyo2.JPG', 'rb')}

		elif number == 10:
			files = {"media" : open('damedesu.jpeg', 'rb')}

		elif number == 11:
			files = {"media" : open('omikuzi_daikyo3.JPG', 'rb')}

		elif number == 12:
			files = {"media" : open('other.JPG', 'rb')}

		elif number == 13:
			files = {"media" : open('omikuzi_kuronuri.jpg', 'rb')}

		elif number == 14:
			files = {"media" : open('omikuzi_kuronuri.jpg', 'rb')}



		req_media = auth2.post(url_media, files = files)

		# レスポンスを確認
		if req_media.status_code != 200:
		    print ("画像アップデート失敗: %s", req_media.text)
		    exit()

		# Media ID を取得
		media_id = json.loads(req_media.text)['media_id']
		print ("Media ID: %d" % media_id)

		# Media ID を付加してテキストを投稿
		params = {'status': '@' + msg["user"]['screen_name'] + '\n#今日の運勢', "media_ids": [media_id]}
		req_media = auth2.post(url_text, params = params)

		# 再びレスポンスを確認
		if req_media.status_code != 200:
		    print ("テキストアップデート失敗: %s", req_text.text)
		    exit()

		print ("OK")
