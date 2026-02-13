

from .BaseApiResponse import BaseApiResponse


class GetPaymentMethodFeesResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.GrossTotal = None
            self.ConvenientFeeAmount = None
            self.ProcessingFeeFixedAmount = None
            self.ProcessingFeeTotal = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.GrossTotal = getattr(obj, 'GrossTotal', None)
                self.ConvenientFeeAmount = getattr(obj, 'ConvenientFeeAmount', None)
                self.ProcessingFeeFixedAmount = getattr(obj, 'ProcessingFeeFixedAmount', None)
                self.ProcessingFeeTotal = getattr(obj, 'ProcessingFeeTotal', None)


