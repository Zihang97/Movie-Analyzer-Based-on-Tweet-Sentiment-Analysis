import pytest
from twitter import grab_tweets

class Testtwtter:
	def test_grap_twitter_no_input(self):
		with pytest.raises(TypeError):
			grab_tweets()

	def test_grap_twitter_1(self):
		tweets=grab_tweets('Tenet',1)
		i=0
		for tweet in tweets:
			i+=1
		assert i == 1

	def test_grap_twitter_5(self):
		tweets=grab_tweets('Tenet',5)
		i=0
		for tweet in tweets:
			i+=1
		assert i == 5

	def test_grap_twitter_10(self):
		tweets=grab_tweets('Tenet',10)
		i=0
		for tweet in tweets:
			i+=1
		assert i == 10


	def test_grap_twitter_20(self):
		tweets=grab_tweets('Tenet',20)
		i=0
		for tweet in tweets:
			i+=1
		assert i == 20
