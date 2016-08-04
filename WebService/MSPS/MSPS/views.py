"""
Routes and views for the flask application.
"""

from flask import render_template
from MSPS import app
from MSPS.MusicCompare import *
from flask import Flask, jsonify, request

mcompare = MusicCompare()

@app.route('/compare', methods=['POST'])
def calculateSimilarity():
	resultsDict = mcompare.compare(request.data, "CS")
	
	return jsonify(resultsDict)