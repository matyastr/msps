from music21 import *
from MSPS.CompareFacade import *

class MusicCompare(object):
	"""Class responsible for initiating all compare operations."""

	def __init__(self):
		self.facade = CompareFacade()

	def compare(self, musicXmlFile, compareTechnique):
		musicXmlConverter = converter.Converter()
		musicStream = musicXmlConverter.parseData(musicXmlFile)
		self.facade.compare(musicStream, compareTechnique)

