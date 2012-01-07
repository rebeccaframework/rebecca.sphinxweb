from pyramid.config import Configurator

def main(global_conf, **settings):
    config = Configurator(settings=settings,
        root_factory='.resources.SphinxWeb')
    config.scan()
    return config.make_wsgi_app()
