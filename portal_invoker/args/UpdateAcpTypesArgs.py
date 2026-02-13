




class UpdateAcpTypesArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Source = None
            self.SourceId = None
            self.CollectMerchantCode = None
            self.DepositClientCode = None
            self.CollectClientCode = None
            self.DepositMerchantCode = None
            self.FeesmerchantCode = None
            self.TibFeesCode = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Source = getattr(obj, 'Source', None)
            self.SourceId = getattr(obj, 'SourceId', None)
            self.CollectMerchantCode = getattr(obj, 'CollectMerchantCode', None)
            self.DepositClientCode = getattr(obj, 'DepositClientCode', None)
            self.CollectClientCode = getattr(obj, 'CollectClientCode', None)
            self.DepositMerchantCode = getattr(obj, 'DepositMerchantCode', None)
            self.FeesmerchantCode = getattr(obj, 'FeesmerchantCode', None)
            self.TibFeesCode = getattr(obj, 'TibFeesCode', None)


