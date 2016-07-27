"""
This script runs the MSPS application using a development server.
Main interaction point with the web service.
"""

from os import environ
from MSPS import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    app.run(HOST, 55360)
