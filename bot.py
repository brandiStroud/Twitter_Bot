from codes import *

authentication = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
authentication.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(authentication)

def __init__(self):
  
