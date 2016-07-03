"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from MSPS import app
from MSPS.MusicCompare import *
from flask import Flask, jsonify

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    },
	{
        'id': 3,
        'title': u'Adding a test',
        'description': u'This is a test', 
        'done': False
    }
]

@app.route('/', methods=['GET'])
@app.route('/compare', methods=['GET'])
def get_tasks():
	#compare = MusicCompare()
	#musicCompare.Compare("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><!DOCTYPE score-partwise PUBLIC \"-//Recordare//DTD MusicXML 3.0 Partwise//EN\" \"http://www.musicxml.org/dtds/partwise.dtd\"><score-partwise version=\"3.0\"><part-list><score-part id=\"P1\"><part-name>Music</part-name></score-part></part-list><part id=\"P1\"><measure number=\"1\"><attributes><divisions>1</divisions><key><fifths>0</fifths></key><time><beats>4</beats><beat-type>4</beat-type></time><clef><sign>G</sign><line>2</line></clef></attributes><note><pitch><step>C</step><octave>4</octave></pitch><duration>4</duration><type>whole</type></note></measure></part></score-partwise>", "CS")
	return jsonify({'tasks': tasks})


#"""
#Routes and views for the flask application.
#"""

#from datetime import datetime
#from flask import render_template
#from FlaskWebProject1 import app

#@app.route('/')
#@app.route('/home')
#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@app.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@app.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
