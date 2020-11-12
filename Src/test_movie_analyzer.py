import pytest
from social_media_analyzer import movie_analyzer

class Testmovieanalyzer:
	def test_movie_analyzer_no_input(self):
		with pytest.raises(TypeError):
			movie_analyzer()

	def test_movie_analyzer_Hocus_Pocus(self):
		assert 6.9 - movie_analyzer("Hocus Pocus",10)[0] < 3 
		
	def test_movie_analyzer_Unhinged(self):
		assert 6.1 - movie_analyzer("Unhinged",10)[0] < 3
		
	def test_movie_analyzer_Tenet(self):
		assert 7.8 - movie_analyzer("Tenet",10)[0] < 3.9
		
	def test_movie_analyzer_Kajillionaire(self):
		assert 6.4 - movie_analyzer("Kajillionaire",10)[0] < 3
