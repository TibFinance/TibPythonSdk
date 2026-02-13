




class ClientLogin:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ClientLoginId = None
            self.Username = None
            self.Firstname = None
            self.Lastname = None
            self.Email = None
            self.LoginType = None
            self.ReferenceType = None
            self.Reference = None
            self.InternalRefernceIds = None
            self.LoginRelationId = None

        else:
            
            self.ClientLoginId = getattr(obj, 'ClientLoginId', None)
            self.Username = getattr(obj, 'Username', None)
            self.Firstname = getattr(obj, 'Firstname', None)
            self.Lastname = getattr(obj, 'Lastname', None)
            self.Email = getattr(obj, 'Email', None)
            self.LoginType = getattr(obj, 'LoginType', None)
            self.ReferenceType = getattr(obj, 'ReferenceType', None)
            self.Reference = getattr(obj, 'Reference', None)
            self.InternalRefernceIds = getattr(obj, 'InternalRefernceIds', None)
            self.LoginRelationId = getattr(obj, 'LoginRelationId', None)


