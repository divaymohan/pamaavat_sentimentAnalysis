import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

consumer_key = "your key"
consumer_secret = "your key"
access_token = "your key"
access_secret = "your key"

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)
class MyListener(StreamListener):

    def on_data(self,data):
        try:
            with open('padmaavat.json','a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" %str(e))
        return True
    def on_error(self,status):
        print(status)
        return  True

twitter_stream = Stream(auth,MyListener())
twitter_stream.filter(track=['Padmaavat','Padmini','Padmavati','padmaavat','padmini','padmavati'])

