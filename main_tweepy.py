import tweepy


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)
        print("--------------")


auth = tweepy.OAuthHandler("vlbop4jIrxEtpFIAmQrgiRcVk", "WR6n7n0HX9sjIyfrxx47ibw13U2ZuKevNzBZYRL3lKTkca6cIM")
auth.set_access_token("814362559-dXkJumv2n28eGSmW5s10ZJXP4wOU2MlY8omJsYGL", "B6TwCGjsoFT7VmEv4DJ6ZQx127Bpo4K0r5lw60uIu7VeZ")

api = tweepy.API(auth)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
#
myStream.filter(track=['@potus'],follow="822215679726100480,25073877,108471631")

#keywords: 

#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)