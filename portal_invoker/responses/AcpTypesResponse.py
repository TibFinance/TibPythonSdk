

from .BaseApiResponse import BaseApiResponse


class AcpTypesResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CollectMerchantCode = None
            self.DepositClientCode = None
            self.CollectClientCode = None
            self.DepositMerchantCode = None
            self.FeesmerchantCode = None
            self.TibFeesCode = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.CollectMerchantCode = getattr(obj, 'CollectMerchantCode', None)
                self.DepositClientCode = getattr(obj, 'DepositClientCode', None)
                self.CollectClientCode = getattr(obj, 'CollectClientCode', None)
                self.DepositMerchantCode = getattr(obj, 'DepositMerchantCode', None)
                self.FeesmerchantCode = getattr(obj, 'FeesmerchantCode', None)
                self.TibFeesCode = getattr(obj, 'TibFeesCode', None)


