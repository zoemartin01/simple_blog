from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.include('pyramid_mako')
        config.include('.security')
        config.include('.routes')
        config.include('.models')
        config.scan()

        session_factory = SignedCookieSessionFactory('secret')
        config.set_session_factory(session_factory)
    return config.make_wsgi_app()
