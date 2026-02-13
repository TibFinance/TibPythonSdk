




class ContractEditionRequest:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ContractEditionRequestId = None
            self.ClientId = None
            self.RequestContent = None
            self.RequestContentPreview = None
            self.CreatedAt = None
            self.ProcessedAt = None
            self.RequestStatus = None
            self.CreatedDate = None
            self.ProcessedDate = None

        else:
            
            self.ContractEditionRequestId = getattr(obj, 'ContractEditionRequestId', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.RequestContent = getattr(obj, 'RequestContent', None)
            self.RequestContentPreview = getattr(obj, 'RequestContentPreview', None)
            self.CreatedAt = getattr(obj, 'CreatedAt', None)
            self.ProcessedAt = getattr(obj, 'ProcessedAt', None)
            self.RequestStatus = getattr(obj, 'RequestStatus', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.ProcessedDate = getattr(obj, 'ProcessedDate', None)


