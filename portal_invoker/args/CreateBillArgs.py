


from ..objects import BillEntity


class CreateBillArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.BillData = None
            self.BreakIfMerchantNeverBeenAuthorized = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.BillData = BillEntity(getattr(obj, 'BillData', None)) if getattr(obj, 'BillData', None) is not None else None
            self.BreakIfMerchantNeverBeenAuthorized = getattr(obj, 'BreakIfMerchantNeverBeenAuthorized', None)


