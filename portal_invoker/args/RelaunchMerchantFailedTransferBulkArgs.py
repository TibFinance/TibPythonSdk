




class RelaunchMerchantFailedTransferBulkArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.TransferIds = None
            self.MerchantId = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)

            self.TransferIds = []
            if hasattr(obj, 'TransferIds') and obj.TransferIds is not None:
                self.TransferIds = [name for name in obj.TransferIds]
            self.MerchantId = getattr(obj, 'MerchantId', None)


