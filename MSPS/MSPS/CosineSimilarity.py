from music21 import *
from MSPS.SimilarityCompareBase import *
from math import *

class CosineSimilarity(SimilarityCompareBase):
	"""Similarity compare implementation for Cosine similarity"""


	def __init__(self):
		pass


	def noteSimilarity(self, inputStream):
		compareDict = {}
		count = 0
		inputVector = self.getVector(inputStream)

		for chorale in corpus.chorales.Iterator():
			otherVector = self.getVector(chorale)
			similarityValue = self.cosignSimilarity(inputVector, otherVector)

			compareDict[chorale.metadata.title + ", Bach"] = similarityValue
			count += 1

			if count == 10:
				break

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

