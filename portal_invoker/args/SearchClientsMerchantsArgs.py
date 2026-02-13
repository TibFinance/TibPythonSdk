




class SearchClientsMerchantsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.SearchText = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.SearchText = getattr(obj, 'SearchText', None)


