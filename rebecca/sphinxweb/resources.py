from sphinx.websupport import WebSupport

class SphinxWeb:
    def __init__(self, request):
        self.request = request
        self.support = WebSupport(datadir=request.registry.settings['rebecca.sphinxweb.datadir'])

    def get_document(self, name):
        return self.support.get_document(name)
