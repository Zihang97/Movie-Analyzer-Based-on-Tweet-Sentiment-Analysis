import pytest
from social_media_analyzer import analyze_sentiment
from social_media_analyzer import movie_analyzer

class Testnlp:
	def test_analyze_sentiment_no_input(self):
		with pytest.raises(TypeError):
			analyze_sentiment()

	def test_analyze_sentiment_empty(self):
		assert analyze_sentiment("")[0] == 0
		assert analyze_sentiment("")[1] == 0

	def test_analyze_sentiment_positive(self):
		assert analyze_sentiment("I'm happy")[0] > 0

	def test_analyze_sentiment_positive2(self):
		assert analyze_sentiment("Today is a great day")[0] > 0

	def test_analyze_sentiment_negative(self):
		assert analyze_sentiment("I'm sad")[0] < 0

	def test_analyze_sentiment_negative2(self):
		assert analyze_sentiment("It's rainy outside")[0] < 0
		
class Testmovieanalyzer:
	def test_movie_analyzer_no_input(self):
		with pytest.raises(TypeError):
			movie_analyzer()

	def test_movie_analyzer_Hocus_Pocus(self):
		assert movie_analyzer("Hocus Pocus",10) < 5
		
	def test_movie_analyzer_Unhinged(self):
		assert movie_analyzer("Unhinged",10) < 5
		
	def test_movie_analyzer_Tenet(self):
		assert movie_analyzer("Tenet",10) > 5
		
	def test_movie_analyzer_Kajillionaire(self):
		assert movie_analyzer("Kajillionaire",10) > 5
