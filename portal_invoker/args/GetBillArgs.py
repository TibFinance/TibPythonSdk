




class GetBillArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.BillId = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.BillId = getattr(obj, 'BillId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


