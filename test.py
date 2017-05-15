import tweepy

consumer_key = 'rYUID44GfWhuOfvBlUbOUR7Ll'
consumer_secret = 'klRhh5xXPEAWbsxD5NtVMEpKh9GCuQZTz39C5lP8sD2M0RbuRU'
access_token = '863867329922420736-AJYgnJsU2DzeSCF3jg1g8tfYaPz5b7r'
access_token_secret = 'Y5U9PQb1jARX6h2x2QxAPjNuNEXKGC3ByXEkIaVM9Y1Co'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


mentions = api.mentions_timeline()
for mention in mentions:
	# print mention
	print mention.geo['coordinates']
   

