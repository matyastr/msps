from music21 import *

class MusicCompare(object):
	"""Class responsible for initiating all compare operations."""
	def __init__(self):
		#MusicCompare.facade = CompareFacade()
		pass
	def Compare(self, musicXmlFile, compareTechnique):
		musicXmlConverter = converter.Converter()
		inputMusicXmlFile = musicXmlConverter.parseData(musicXmlFile)

