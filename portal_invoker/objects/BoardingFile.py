




class BoardingFile:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DocType = None
            self.DocsReceived = None
            self.DocLimit = None
            self.DocGenericDescription = None
            self.DocStatus = None

        else:
            
            self.DocType = getattr(obj, 'DocType', None)
            self.DocsReceived = getattr(obj, 'DocsReceived', None)
            self.DocLimit = getattr(obj, 'DocLimit', None)
            self.DocGenericDescription = getattr(obj, 'DocGenericDescription', None)
            self.DocStatus = getattr(obj, 'DocStatus', None)


