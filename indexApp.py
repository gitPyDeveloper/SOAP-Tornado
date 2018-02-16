
#Flask is a web application framework written in Python. Armin Ronacher
#Flask is based on Werkzeug WSGI toolkit and Jinja2 template engine

'''
Web Server Gateway Interface (WSGI) has been adopted as a standard for Python web application development. 
WSGI is a specification for a universal interface between the web server and the web applications.
'''

from flask import Flask
app = Flask(__name__)

#The route() decorator in Flask is used to bind URL to a function
@app.route('/')
def index():
    return "home page"




if __name__ == '__main__':
    #app.run(host, port, debug, options)
    #host - default to localhost [127.0.0.1]
    #port - default 5000
    #debug - Defaults to false
    #options - To be forwarded to underlying Werkzeug server.
    app.run()
