# Movie-Analyzer-Based-on-Tweet-Sentiment-Analysis
This is a social media analyzer which can judge the quality of movies based on sentiment analysis in related tweets.

## Description 
People sometimes will tweet after watching movies to express their opinions about the movies. Based on that, I designed this movie analyzer according to the sentiment analysis of the movie-related tweets. For each movies, I pick 1000 relevant tweets and use google NLP API to analyze their sentiment. The sentiment score is -1~1 and I scale it to 0-10 as the score of movies. If overall sentiment is less than 0, the score of movies will be less than 5. In contrary, the score of movies will be larger than 5 if overall sentiment is larger than 0. Afterwards I will compare the score from my movie analyzer to the score in IMDB to see the effect of my analyzer.

### MVP (Minimum Value Product)
The basic function of movie analyzer is grabbing the tweets and analyzing the sentiment of texts.

### User Story
As a cinema manager, I want to see the score of each movie on show based on the analysis of people's feeling so that I can schedule the showtimes of movies tomorrow.

As a movies promotion manager, I want to see people's feedback about the movie so that I can adjust the promotion strategy according to people's feeling.

As a film viewer, I want to see what other people feel about the movie and if there is someone having the same feeling as mine.


## Design
The movie analyzer uses tweepy, a common tweet API, and google NLP API.

### Grab the relevant tweets
```
alltweets = tweepy.Cursor(api.search,q='Tenet',lang='en').items(1000)
```

### Analyze the sentiment
```
document = {"content": tweet, "type": type_, "language": language}
response = client.analyze_sentiment(document, encoding_type=encoding_type)
```

### A simple example
I use this simple example to see if the movie analyzer works. I pick one tweet about Tenet to see its results.
