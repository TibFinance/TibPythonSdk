




class ApplyChangeValidationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.ValidationToken = None
            self.ChangeApproved = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.ValidationToken = getattr(obj, 'ValidationToken', None)
            self.ChangeApproved = getattr(obj, 'ChangeApproved', None)


