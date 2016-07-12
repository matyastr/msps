from music21 import *
from MSPS.CompareFacade import *

class MusicCompare(object):
	"""Class responsible for initiating all compare operations."""


	def __init__(self):
		self.facade = CompareFacade()


	def compare(self, musicXmlFile, compareTechnique):
		musicStream = converter.parseData(musicXmlFile)
		compareDict = self.facade.compare(musicStream, compareTechnique)

		resultsDict = {}

		inputTitle = ""
		inputComposer = ""

		if musicStream.metadata.title != None:
			inputTitle = musicStream.metadata.title

		if musicStream.metadata.composer != None:
			inputComposer = musicStream.metadata.composer

		resultsDict["Input"] = inputTitle + ", " + inputComposer
		resultsDict["Similarity Results"] = compareDict

		return resultsDict