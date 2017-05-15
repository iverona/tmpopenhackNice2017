from twitter_auth import auth, api
import tweepy
from twitter_streamer import MyListener
from twitter_streamer import MyManager


manager = MyManager(api)
twitter_stream = tweepy.Stream(auth, MyListener("python.json", manager))
twitter_stream.filter(track=['@RHIME_OpenHack'])




