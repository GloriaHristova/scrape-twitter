# Load necessary modules and packages
import tweepy
import authenticate
import scrapeoptions
from tweepy import Stream
from tweepy.streaming import StreamListener

# Authenticate with Twitter using tweepy (must create a Twitter Application - check read.me)
auth = tweepy.OAuthHandler(authenticate.api_key, authenticate.api_Secret)
auth.set_access_token(authenticate.access_token, authenticate.access_token_secret)
api = tweepy.API(auth)

# Rewrite the StreamListener() class (for more details - check tweepy documentation and repo - https://github.com/tweepy/tweepy)
# Make use of on_data() method of StreamListener() class in order to obtain raw data from Twitter Streaming API 
# More about the Tweet() object - https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object

class MyListener(StreamListener):
    
    def __init__(self,limit=10):
        
        super().__init__()
        self.counter = 0
        self.limit = limit
     
    def on_data(self, data):

        # ! Retweets and quoted tweets are EXCLUDED from the sample
        if 'retweeted_status' in data: 
            return

        if 'quoted_status' in data: 
            return
        
        self.counter += 1
        
        # Append each new tweet to json
        try:
            with open(scrapeoptions.nameoutputfile, 'a') as f:
                f.write(data) 
        except:
            print("Error: on_data.")
             
        # Disconnect if set limit is exceeded
        if self.counter < self.limit:
            return True
        else:
            return False
 
    def on_error(self, status):
        print(status)
        # Disconnect if we are rate limited from Twitter
        if status == 420: 
            return False

# Start the listener   
stream_listener =  MyListener(limit = scrapeoptions.setlimit) # the default limit is 10 tweets
twitter_stream = Stream(auth,stream_listener)
twitter_stream.filter(track=scrapeoptions.keywords, languages = scrapeoptions.tweetlang)
print("Your tweets are ready.")