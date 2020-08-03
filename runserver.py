"""
This script runs the clinicsync API application using a development server.
"""

from os import environ,system
from clinicsync import app
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    # app.run(port=5002, threaded=False)

    # Serve the app with gevent
    http_server = WSGIServer(('0.0.0.0', 5000), app)
    http_server.serve_forever()
