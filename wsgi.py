import os

virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
try:
  exec_namespace = dict(__file__=virtualenv)
  with open(virtualenv, 'rb') as exec_file:
    file_contents = exec_file.read()
  compiled_code = compile(file_contents, virtualenv, 'exec')
  exec(compiled_code, exec_namespace)
except IOError:
  pass

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