


from ..enums import TibAuthorizationStatus
from ..enums import ClientAuthorizationStatus


class TransferValidationEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Amount = None
            self.CreatedDate = None
            self.AcountNumber = None
            self.ExternalReferenceNumber = None
            self.GroupId = None
            self.TibAuthorization = None
            self.TibAuthorizationStatusStr = None
            self.ClientAuthorization = None
            self.ClientAuthorizationStatusStr = None
            self.MerchantName = None
            self.CustomerName = None
            self.Bill = None
            self.TransferType = None
            self.TransferId = None
            self.CustomerId = None
            self.DueDate = None

        else:
            
            self.Amount = getattr(obj, 'Amount', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.AcountNumber = getattr(obj, 'AcountNumber', None)
            self.ExternalReferenceNumber = getattr(obj, 'ExternalReferenceNumber', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.TibAuthorization = TibAuthorizationStatus(getattr(obj, 'TibAuthorization', None)) if getattr(obj, 'TibAuthorization', None) is not None else None
            self.TibAuthorizationStatusStr = getattr(obj, 'TibAuthorizationStatusStr', None)
            self.ClientAuthorization = ClientAuthorizationStatus(getattr(obj, 'ClientAuthorization', None)) if getattr(obj, 'ClientAuthorization', None) is not None else None
            self.ClientAuthorizationStatusStr = getattr(obj, 'ClientAuthorizationStatusStr', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.Bill = getattr(obj, 'Bill', None)
            self.TransferType = getattr(obj, 'TransferType', None)
            self.TransferId = getattr(obj, 'TransferId', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.DueDate = getattr(obj, 'DueDate', None)


