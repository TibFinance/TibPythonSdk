




class GetTransferBatchResultArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.BatchId = None
            self.FromIndex = None
            self.MaxItems = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.BatchId = getattr(obj, 'BatchId', None)
            self.FromIndex = getattr(obj, 'FromIndex', None)
            self.MaxItems = getattr(obj, 'MaxItems', None)


