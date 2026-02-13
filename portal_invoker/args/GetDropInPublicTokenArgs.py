


from ..enums import TransferType
from ..enums import AutorizedPaymentMethodFlags
from ..enums import Language


class GetDropInPublicTokenArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.CustomerId = None
            self.BillId = None
            self.Amount = None
            self.TransferType = None
            self.DropInAuthorizedPaymentMethod = None
            self.ExternalReferenceNumber = None
            self.ShowCustomerExistingPaymentMethods = None
            self.Language = None
            self.ExpirationDays = None
            self.Title = None
            self.Description = None
            self.PaymentDueDate = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.BillId = getattr(obj, 'BillId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.DropInAuthorizedPaymentMethod = AutorizedPaymentMethodFlags(getattr(obj, 'DropInAuthorizedPaymentMethod', None)) if getattr(obj, 'DropInAuthorizedPaymentMethod', None) is not None else None
            self.ExternalReferenceNumber = getattr(obj, 'ExternalReferenceNumber', None)
            self.ShowCustomerExistingPaymentMethods = getattr(obj, 'ShowCustomerExistingPaymentMethods', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.ExpirationDays = getattr(obj, 'ExpirationDays', None)
            self.Title = getattr(obj, 'Title', None)
            self.Description = getattr(obj, 'Description', None)
            self.PaymentDueDate = getattr(obj, 'PaymentDueDate', None)


