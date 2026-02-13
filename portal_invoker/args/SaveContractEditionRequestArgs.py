




class SaveContractEditionRequestArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.RequestContent = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.RequestContent = getattr(obj, 'RequestContent', None)


