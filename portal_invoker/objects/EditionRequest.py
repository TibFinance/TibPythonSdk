


from ..enums import ContractRequestStatus


class EditionRequest:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Content = None
            self.Status = None
            self.CreationDate = None

        else:
            
            self.Content = getattr(obj, 'Content', None)
            self.Status = ContractRequestStatus(getattr(obj, 'Status', None)) if getattr(obj, 'Status', None) is not None else None
            self.CreationDate = getattr(obj, 'CreationDate', None)


