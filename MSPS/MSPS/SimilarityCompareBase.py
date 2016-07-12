from abc import ABCMeta, abstractmethod

class SimilarityCompareBase():
	"""description of class"""
	__metaclass__ = ABCMeta

	@abstractmethod
	def compare(self):
		pass

