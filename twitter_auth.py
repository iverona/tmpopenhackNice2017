import tweepy
from tweepy import OAuthHandler


# Marcos
consumer_key = 'GT89J1m2w9cjjXfGVK4rVglKM'
consumer_secret = 'OBq8PuvuTiyz9igzEJxNmsoe3kyo6RQe7CgJBg3h7h42oquyDN'
access_token = '863804439945244672-e7fBxFVCDXt3GZbcWPDUoTLq38tI9c3'
access_secret = 'WoIeUv1gOM4NfWxU6tdwCKes2RaUF1t6Jry86MgQIBTfx'

# consumer_key = 'rYUID44GfWhuOfvBlUbOUR7Ll'
# consumer_secret = 'klRhh5xXPEAWbsxD5NtVMEpKh9GCuQZTz39C5lP8sD2M0RbuRU'
# access_token = '863867329922420736-AJYgnJsU2DzeSCF3jg1g8tfYaPz5b7r'
# access_secret = 'Y5U9PQb1jARX6h2x2QxAPjNuNEXKGC3ByXEkIaVM9Y1Co'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)