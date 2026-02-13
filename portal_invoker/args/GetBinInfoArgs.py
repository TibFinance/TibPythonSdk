




class GetBinInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Bin = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Bin = getattr(obj, 'Bin', None)


