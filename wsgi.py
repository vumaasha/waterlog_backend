import os
import sys

here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(here, 'waterlog_py'))
config = os.path.join(here,'production.ini')


import logging.config
logging.config.fileConfig(config)

from pyramid.paster import get_app
application = get_app(config, 'main')

if __name__  == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, application)
    httpd.handle_request()