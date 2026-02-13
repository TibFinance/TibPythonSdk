




class DeleteRecuringTransferArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.RecuringTransferId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.RecuringTransferId = getattr(obj, 'RecuringTransferId', None)


