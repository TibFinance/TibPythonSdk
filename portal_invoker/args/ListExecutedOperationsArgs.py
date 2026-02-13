


from ..enums import TransferTypeFlag
from ..enums import DateType


class ListExecutedOperationsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.FromDate = None
            self.ToDate = None
            self.TransferType = None
            self.TransferGroupId = None
            self.OnlyWithErrors = None
            self.MerchantId = None
            self.DateType = None
            self.ServiceId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.TransferType = TransferTypeFlag(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.TransferGroupId = getattr(obj, 'TransferGroupId', None)
            self.OnlyWithErrors = getattr(obj, 'OnlyWithErrors', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.DateType = getattr(obj, 'DateType', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)


