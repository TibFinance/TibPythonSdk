

from .BaseEventPayload import BaseEventPayload


class TransactionEventPayload(BaseEventPayload):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Target = None
            self.Direction = None
            self.Step = None
            self.Status = None
            self.DescriptionCode = None
            self.Description = None
            self.Amount = None
            self.MerchantId = None
            self.MerchantName = None
            self.MerchantAccountPreview = None
            self.MerchantExternalId = None
            self.MerchantDescription = None
            self.TransferPayload = None

        else:
            super().__init__(obj)

            from .TransferPayload import TransferPayload
            self.Target = getattr(obj, 'Target', None)
            self.Direction = getattr(obj, 'Direction', None)
            self.Step = getattr(obj, 'Step', None)
            self.Status = getattr(obj, 'Status', None)
            self.DescriptionCode = getattr(obj, 'DescriptionCode', None)
            self.Description = getattr(obj, 'Description', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantAccountPreview = getattr(obj, 'MerchantAccountPreview', None)
            self.MerchantExternalId = getattr(obj, 'MerchantExternalId', None)
            self.MerchantDescription = getattr(obj, 'MerchantDescription', None)

            self.TransferPayload = []
            if hasattr(obj, 'TransferPayload') and obj.TransferPayload is not None:
                self.TransferPayload = [TransferPayload(name) for name in  obj.TransferPayload]


