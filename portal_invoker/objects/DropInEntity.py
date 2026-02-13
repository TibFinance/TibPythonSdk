


from ..enums import TransferType
from ..enums import AutorizedPaymentMethodFlags


class DropInEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerExistingsPayments = None
            self.Amout = None
            self.TransferType = None
            self.AuthorizedPaymentMode = None
            self.ExternalReferenceNumber = None
            self.Title = None
            self.Description = None
            self.PaymentDueDate = None
            self.MerchantId = None
            self.ServiceId = None
            self.MerchantName = None
            self.MerchantPhone = None
            self.MerchantEmail = None
            self.RequestPPAFromCustomer = None

        else:
            
            from .PaymentMethod import PaymentMethod

            self.CustomerExistingsPayments = []
            if hasattr(obj, 'CustomerExistingsPayments') and obj.CustomerExistingsPayments is not None:
                self.CustomerExistingsPayments = [PaymentMethod(name) for name in  obj.CustomerExistingsPayments]
            self.Amout = getattr(obj, 'Amout', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.AuthorizedPaymentMode = AutorizedPaymentMethodFlags(getattr(obj, 'AuthorizedPaymentMode', None)) if getattr(obj, 'AuthorizedPaymentMode', None) is not None else None
            self.ExternalReferenceNumber = getattr(obj, 'ExternalReferenceNumber', None)
            self.Title = getattr(obj, 'Title', None)
            self.Description = getattr(obj, 'Description', None)
            self.PaymentDueDate = getattr(obj, 'PaymentDueDate', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantPhone = getattr(obj, 'MerchantPhone', None)
            self.MerchantEmail = getattr(obj, 'MerchantEmail', None)
            self.RequestPPAFromCustomer = getattr(obj, 'RequestPPAFromCustomer', None)


