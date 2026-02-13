




class BoardingDocument:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Status = None
            self.DocUnderWriterNotes = None
            self.DocType = None
            self.DocsReceived = None
            self.DocLimit = None
            self.DocGenericDescription = None

        else:
            
            self.Status = getattr(obj, 'Status', None)
            self.DocUnderWriterNotes = getattr(obj, 'DocUnderWriterNotes', None)
            self.DocType = getattr(obj, 'DocType', None)
            self.DocsReceived = getattr(obj, 'DocsReceived', None)
            self.DocLimit = getattr(obj, 'DocLimit', None)
            self.DocGenericDescription = getattr(obj, 'DocGenericDescription', None)


