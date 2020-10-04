# coding: utf-8
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import tweepy

consumer_key = "Enter the consumer_key"
consumer_secret = "Enter the consumer_secret"
access_key = "Enter the access_key"
access_secret = "Enter the access_secret"
filmname = "Enter the filmname you want to judge"
tweets_number = "Enter the number of tweets you want to judge from"

def grab_tweets(film,number):
    # authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)

    api = tweepy.API(auth,wait_on_rate_limit=True)
    
    # search the relevant tweets 
    alltweets = tweepy.Cursor(api.search,q=film,lang='en',result_type='recent').items(number)
    return alltweets


def sample_analyze_sentiment(tweet):
    client = language_v1.LanguageServiceClient()

    # Available types: PLAIN_TEXT, HTML
    type_ = enums.Document.Type.PLAIN_TEXT
    # the language of the tweet you grabed
    language = "en"
    
    document = {"content": tweet, "type": type_, "language": language}
    
    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = enums.EncodingType.UTF8
    
    # analyze the sentiment of tweet
    response = client.analyze_sentiment(document, encoding_type=encoding_type)
    
    # return overall sentiment of the input document
    return [response.document_sentiment.score,response.document_sentiment.magnitude]

if __name__ == '__main__':
    scores,magnitudes=[],[]
    
    # get relevant tweets
    tweets=grab_tweets(filmname,tweets_number)
    
    for tweet in tweets:
        # analyze each tweet
        scores+=[sample_analyze_sentiment(tweet.text)[0]]
        magnitudes+=[sample_analyze_sentiment(tweet.text)[1]]
    
    # compute the averages
    finalscore=(sum(scores)/len(scores))*5+5
    finalmagnitude=sum(magnitudes)/len(magnitudes)
    
    # print the final outputs
    print("The score of movie",filmname,"is", finalscore)
    print("The magnitude of movie",filmname,"is", finalmagnitude)


