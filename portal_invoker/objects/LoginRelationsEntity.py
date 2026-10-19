




class LoginRelationsEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.LoginsUserRelationsId = None
            self.InternalReferenceType = None
            self.InternalReferenceId = None
            self.Description = None
            self.IsReadOnly = None

        else:
            
            self.LoginsUserRelationsId = getattr(obj, 'LoginsUserRelationsId', None)
            self.InternalReferenceType = getattr(obj, 'InternalReferenceType', None)
            self.InternalReferenceId = getattr(obj, 'InternalReferenceId', None)
            self.Description = getattr(obj, 'Description', None)
            self.IsReadOnly = getattr(obj, 'IsReadOnly', None)


