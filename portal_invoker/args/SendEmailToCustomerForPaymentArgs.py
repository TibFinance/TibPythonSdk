


from ..enums import TransferType


class SendEmailToCustomerForPaymentArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.TransferType = None
            self.DropInPublicTokenId = None
            self.Email = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.DropInPublicTokenId = getattr(obj, 'DropInPublicTokenId', None)
            self.Email = getattr(obj, 'Email', None)


