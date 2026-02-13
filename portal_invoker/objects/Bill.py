

from .BillEntity import BillEntity


class Bill(BillEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BillId = None
            self.ConvenientFeeCreditCard = None
            self.ConvenientFeeDirectAccount = None
            self.CreatedDate = None

        else:
            super().__init__(obj)

            self.BillId = getattr(obj, 'BillId', None)
            self.ConvenientFeeCreditCard = getattr(obj, 'ConvenientFeeCreditCard', None)
            self.ConvenientFeeDirectAccount = getattr(obj, 'ConvenientFeeDirectAccount', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)


