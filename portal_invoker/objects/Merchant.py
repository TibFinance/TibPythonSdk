

from .MerchantBasicInfo import MerchantBasicInfo


class Merchant(MerchantBasicInfo):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Account = None

        else:
            super().__init__(obj)
            from .Account import Account
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None


