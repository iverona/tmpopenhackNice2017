import tweepy
from tweepy import OAuthHandler

consumer_key = 'GT89J1m2w9cjjXfGVK4rVglKM'
consumer_secret = 'OBq8PuvuTiyz9igzEJxNmsoe3kyo6RQe7CgJBg3h7h42oquyDN'
access_token = '863804439945244672-e7fBxFVCDXt3GZbcWPDUoTLq38tI9c3'
access_secret = 'WoIeUv1gOM4NfWxU6tdwCKes2RaUF1t6Jry86MgQIBTfx'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)