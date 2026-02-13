




class UpdateContractEditionRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.ContractEditionRequestId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.ContractEditionRequestId = getattr(obj, 'ContractEditionRequestId', None)


