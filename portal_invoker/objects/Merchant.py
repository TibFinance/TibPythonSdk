

from .MerchantBasicInfo import MerchantBasicInfo


class Merchant(MerchantBasicInfo):
    def __init__(self, obj=None):
        super().__init__(obj)
        if obj is None:
            self.Account = None
        else:
            from .Account import Account
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None
