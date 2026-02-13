

from .BaseEventPayload import BaseEventPayload


class TransferPendingProcessPayload(BaseEventPayload):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ServiceId = None
            self.ServiceName = None
            self.MerchantId = None
            self.MerchantExternalSystemId = None
            self.MerchantExternalSystemGroupId = None
            self.MerchantName = None
            self.IsAutomaticPayment = None
            self.PaymentInfo = None
            self.IsMarkResolved = None
            self.CurrentStatus = None
            self.CreatedDate = None
            self.PaymentMethodDescription = None
            self.AccountInformationPreview = None
            self.PaymentMethodType = None
            self.PreCalculatedFees = None

        else:
            super().__init__(obj)

            from .TransferPayload import TransferPayload
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantExternalSystemId = getattr(obj, 'MerchantExternalSystemId', None)
            self.MerchantExternalSystemGroupId = getattr(obj, 'MerchantExternalSystemGroupId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.IsAutomaticPayment = getattr(obj, 'IsAutomaticPayment', None)
            self.PaymentInfo = TransferPayload(getattr(obj, 'PaymentInfo', None)) if getattr(obj, 'PaymentInfo', None) is not None else None
            self.IsMarkResolved = getattr(obj, 'IsMarkResolved', None)
            self.CurrentStatus = getattr(obj, 'CurrentStatus', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.PaymentMethodDescription = getattr(obj, 'PaymentMethodDescription', None)
            self.AccountInformationPreview = getattr(obj, 'AccountInformationPreview', None)
            self.PaymentMethodType = getattr(obj, 'PaymentMethodType', None)
            self.PreCalculatedFees = getattr(obj, 'PreCalculatedFees', None)


