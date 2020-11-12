import tweepy
import os

access_key = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')

def grab_tweets(film,number):
    # authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    # search the relevant tweets 
    alltweets = tweepy.Cursor(api.search,q=film,lang='en',result_type='recent').items(number)
    return alltweets
