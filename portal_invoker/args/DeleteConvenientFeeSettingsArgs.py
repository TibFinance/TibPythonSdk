




class DeleteConvenientFeeSettingsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Id = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Id = getattr(obj, 'Id', None)


