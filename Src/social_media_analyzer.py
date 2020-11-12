# coding: utf-8
from google.cloud import language_v1
from google.cloud.language_v1 import enums
import tweepy
import os
from twitter import grab_tweets

filmname = "Enter the filmname you want to judge"
tweets_number = "Enter the number of tweets you want to judge from"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "cloud_natural_language_api.json"
    
def analyze_sentiment(tweet):
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


def movie_analyzer(filmname,tweets_number):
    scores,magnitudes=[],[]
    
    # get relevant tweets
    tweets=grab_tweets(filmname,tweets_number)
    
    for tweet in tweets:
        # analyze each tweet
        scores+=[analyze_sentiment(tweet.text)[0]]
        magnitudes+=[analyze_sentiment(tweet.text)[1]]
    
    # compute the averages
    finalscore=(sum(scores)/len(scores))*5+5
    finalmagnitude=sum(magnitudes)/len(magnitudes)
    
    return [finalscore, finalmagnitude]

if __name__ == '__main__':
    output=movie_analyzer(filmname,tweets_number)
    
    # print the final outputs
    print(f"The score of movie {filmname} is", output[0])
    print(f"The magnitude of movie {filmname} is", output[1])
