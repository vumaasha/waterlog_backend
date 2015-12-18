from pyramid.config import Configurator
from sqlalchemy import engine_from_config
import os

from .models import (
    DBSession,
    Base,
    )

def expandvars_dict(settings):
    """Expands all environment variables in a settings dictionary."""
    return dict((key, os.path.expandvars(value)) for
                key, value in settings.items())

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    settings = expandvars_dict(settings)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('cornice')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
