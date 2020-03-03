import os
import tweepy as tw 
import pandas as pd
import re

API_key= 'BNBcJIAN5eQXYMRExMoX6McG9'
API_secret_key= 'hXMEXkEjwEnGJaNQgZ6MN048eRwSGUubnbyXMc2sHgY1bDalFl'
access_token= '1232552940910432257-gFm2ZPyrwhIK0P4a8W9CyMJar98j8D'
access_token_secret= 'AzmHwez2nR1v69HJYY3evjW9pvz0s3Z49u8Lb4WlRlrRQ'

auth = tw.OAuthHandler(API_key, API_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tw.API(auth, wait_on_rate_limit=True)
#api.get_user()this is used to take th timeline for given users
user = api.get_user('@rajinikanth')
timeline=tw.Cursor(api.user_timeline, id="@rajinikanth")
for line in timeline.pages():
	#print(str(line))
	for word in line:
		word=str(word)
		words=word.split(',')
		#print(words)
		for wo in words:
			#if type(wo)
			ch=wo.split(':')
			ch=' '.join(ch)
			ch=ch.replace("'",'')
			ch=ch.split(' ',2)
			if ch[1]=='text':#This if statement is used to print the user name and the tweet
				print(ch[1::])
				input()
			elif ch[1]=='name':
				print(ch[1::])
				input()
			