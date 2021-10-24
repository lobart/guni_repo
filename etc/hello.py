import multiprocessing
from wsgiref.simple_server import make_server
from web.hello import application
httpd = make_server('0.0.0.0', 8080, application)
httpd.serve_forever()