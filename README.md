# Unit Test
I use pytest to test my movie analyzer. The details can be seen in [Actions](https://github.com/Zihang97/Movie-Analyzer-Based-on-Tweet-Sentiment-Analysis/actions).

For both twitter and google nlp functions I use multiple test cases including no input, empty string and other conditions. 

Totally I wrote three test files which can be seen in [src](src/), including test_twitter.py for twitter testing, test_nlp.py for google nlp testing and test_movie_analyzer for whole model testing.

# Movie-Analyzer-Based-on-Tweet-Sentiment-Analysis
This is a social media analyzer which can judge the quality of movies based on sentiment analysis in relevant tweets.

## Description 
People sometimes will tweet after watching movies to express their opinions about the movies. Based on that, I designed this movie analyzer according to the sentiment analysis of the movie-related tweets. For each movies, you can pick any number of relevant tweets and use google NLP API to analyze their sentiment. The sentiment score is -1~1 and I scale it to 0-10 as the score of movies. If overall sentiment is less than 0, the score of movies will be less than 5. In contrary, the score of movies will be larger than 5 if overall sentiment is larger than 0. Afterwards I will compare the score from my movie analyzer to the score in IMDB to see the effect of my analyzer.

### MVP (Minimum Value Product)
The basic function of movie analyzer is grabbing the tweets and analyzing the sentiment of texts.

### User Story
As a cinema manager, I want to see the score of each movie playing based on the analysis of people's feeling so that I can schedule the showtimes of movies tomorrow.

As a movies promotion manager, I want to see people's feedback about the movie so that I can adjust the promotion strategy according to people's feeling.

As a film viewer, I want to see what other people feel about the movie and if there is someone having the same feeling as mine.


## Design
The movie analyzer uses tweepy and google NLP API.

### Grab the relevant tweets
```
api = tweepy.API(auth)
alltweets = tweepy.Cursor(api.search,q=film,lang='en').items(number)
```

### Analyze the sentiment
```
document = {"content": tweet, "type": type_, "language": language}
response = client.analyze_sentiment(document, encoding_type=encoding_type)
```

### A simple example
I use this simple example to see if the movie analyzer works. I pick one tweet about Tenet to see its results.

<p align="left">
    <img src="https://github.com/Zihang97/Movie-Analyzer-Based-on-Tweet-Sentiment-Analysis/blob/main/Picture/simple%20example.PNG" width="600"/>
</p>

## Results
Here is the results for some movies playing. Each movies I use 100 tweets to judge as my computer run quite slowly.

| Movie  | Score   |IMDb |
|------  |---------|-----|
| Tenet  | 5.35    | 7.8 |
|Hocus Pocus| 4.9   | 6.9 |
|Kajillionaire|  5.6  | 6.4 |
|Unhinged |   4.5      | 6.1|

I find that the score of movie analyzer is close to 5, which means that most people wouldn't show very strong emotions about moives. There exists some difference between my scores and IMDb scores. The reasons may lie in that I only use 100 tweets for each movies, I should scale more properly like 0 to 7 and people tend to be more straightforward in tweet rather than IMDb. So many people may show negtive sentiment on tweet, but don't rate low scores on IMDb.
