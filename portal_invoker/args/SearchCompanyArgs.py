




class SearchCompanyArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.text = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.text = getattr(obj, 'text', None)


