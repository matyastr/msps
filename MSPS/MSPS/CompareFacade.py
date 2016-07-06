from music21 import *
from MSPS.CosineSimilarity import *

class CompareFacade(object):
	"""In charge of directing which comparison technique to use."""

	def __init__(self):
		self.cosineCompare = SimilarityCompare()

	def compare(self, stream, technique):
		if technique == 'cs':
			self
		
			