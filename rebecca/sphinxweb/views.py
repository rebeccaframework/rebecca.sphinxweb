from pyramid.view import view_config

class SphinxWebView:
    def __init__(self, context, request):
        self.context = context
        self.request = request

    @view_config(context='.resources.SphinxWeb', 
        renderer='index.mak')
    def index(self):
        document = self.context.get_document('index')
        return dict(document=document)
