import tweepy
import urllib.request
import API_Tokens as token
import user_info as user

def timeline_images(api, target):
    for status in tweepy.Cursor(api.user_timeline, id = target).items(10):
        print(status.entities)
        
