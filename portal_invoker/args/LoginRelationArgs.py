




class LoginRelationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.InternalReferenceId = None
            self.InternalReferenceType = None
            self.LoginId = None
            self.Description = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.InternalReferenceId = getattr(obj, 'InternalReferenceId', None)
            self.InternalReferenceType = getattr(obj, 'InternalReferenceType', None)
            self.LoginId = getattr(obj, 'LoginId', None)
            self.Description = getattr(obj, 'Description', None)


