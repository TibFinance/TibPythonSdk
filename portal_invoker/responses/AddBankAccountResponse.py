

from .BaseApiResponse import BaseApiResponse


class AddBankAccountResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.NewMerchantId = None

        else:
            super().__init__(obj)
            self.NewMerchantId = getattr(obj, 'NewMerchantId', None)


