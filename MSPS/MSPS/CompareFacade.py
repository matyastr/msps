from music21 import *
from MSPS.CosineSimilarity import *

class CompareFacade(object):
	"""In charge of directing which comparison technique to use."""


	def __init__(self):
		self.cosineCompare = CosineSimilarity()


	def compare(self, inputStream, technique):
		compareDict = []

		if technique == 'CS':
			compareDict = self.cosineCompare.compare(inputStream)

		return compareDict

		
		
		
			