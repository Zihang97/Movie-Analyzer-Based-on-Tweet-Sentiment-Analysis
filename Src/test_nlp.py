import pytest
from social_media_analyzer import analyze_sentiment

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

