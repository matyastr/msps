from music21 import *
from MSPS.SimilarityCompareBase import *
from math import *
import time

class CosineSimilarity(SimilarityCompareBase):
	"""Similarity compare implementation for Cosine similarity"""

	_corpus = {}
	_lock = 0

	def __init__(self):	
		lock = 1

		count = 0
		
		
		a = corpus.getBachChorales()

		f = len(a)

		##self.FillCorpus('xml')


		for chorale in corpus.chorales.Iterator():
			self._corpus[chorale.metadata.title + "|Bach"] = chorale

		lock = 0

	def FillCorpus(self, fileExtension):
		coreCorpus = corpus.corpora.CoreCorpus()
		corpusFilePaths = coreCorpus.getPaths(fileExtension)

		count = 0

		for file in corpusFilePaths:
			parsedScore = converter.parse(file)

			title = "Anonymous"
			composer = "Anonymous"

			if parsedScore.metadata.title != None:
				title = parsedScore.metadata.title

			if parsedScore.metadata.composer != None:
				composer = parsedScore.metadata.composer

			key = title + " | " + composer

			if self._corpus.__contains__(key):
				key = fileExtension + count 

			self._corpus[title + " | " + composer] = parsedScore
			count += 1


	def noteSimilarity(self, inputStream):
		while self._lock != 0:
			time.sleep(1)

		

		compareDict = {}
		count = 0
		inputVector = self.getVector(inputStream)

		for title, score in self._corpus.iteritems():
			otherVector = self.getVector(score)
			similarityValue = self.cosignSimilarity(inputVector, otherVector)

			compareDict[title] = similarityValue

		return compareDict


	def getVector(self, inputStream):
		vector = []

		for i in range(12):
			vector.append(0)

		for pitch in inputStream.pitches:
			vector[pitch.pitchClass] += 1

		return vector


	def compare(self, inputStream):
		return self.noteSimilarity(inputStream)


	"""Credit given to http://dataconomy.com/implementing-the-five-most-popular-similarity-measures-in-python/"""
	def calculateSquareRoot(self, vector):
		return round(sqrt(sum([item*item for item in vector])),3)


	"""Credit given to http://dataconomy.com/implementing-the-five-most-popular-similarity-measures-in-python/"""
	def cosignSimilarity(self, vector1, vector2):
		numerator = sum(a*b for a,b in zip(vector1, vector2))
		denominator = self.calculateSquareRoot(vector1) * self.calculateSquareRoot(vector2)
		return round(numerator / float(denominator), 3)

