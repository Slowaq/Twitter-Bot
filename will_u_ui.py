import tweepy
from time import *
import os
from datetime import datetime

print('this is my twitter bot', flush=True)

CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'
ACCESS_KEY = 'ACCESS_KEY'
ACCESS_SECRET = 'ACCESS_SECRET'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

timi = 2 

def reply_to_tweets():
    
    api.update_status("trumturuuum, current time is: "+datetime.now().strftime('%Y-%m-%d %H:%M'))
    print("trumturuuum, current time is: "+datetime.now().strftime('%Y-%m-%d %H:%M'))
    
while True:
    
 
    reply_to_tweets()
    
    sleep(3600)

