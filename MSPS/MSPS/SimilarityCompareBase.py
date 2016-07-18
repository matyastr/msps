from abc import ABCMeta, abstractmethod

class SimilarityCompareBase():
	"""Abstract class for general compare classes."""
	__metaclass__ = ABCMeta

	@abstractmethod
	def compare(self, inputStream):
		pass

