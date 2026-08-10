
from ..utility import to_enum

from ..enums import PaymentFilterLevel
from ..enums import TransferTypeFlag


class ListTransfersArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.PaymentFilterLevel = None
            self.LevelFilterId = None
            self.MarkResolvedOnly = None
            self.FromDate = None
            self.ToDate = None
            self.TransferGroupId = None
            self.TransferType = None
            self.ExternalMerchantGroupId = None
            self.OnlyWithErrors = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.PaymentFilterLevel = to_enum(PaymentFilterLevel, getattr(obj, 'PaymentFilterLevel', None))
            self.LevelFilterId = getattr(obj, 'LevelFilterId', None)
            self.MarkResolvedOnly = getattr(obj, 'MarkResolvedOnly', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.TransferGroupId = getattr(obj, 'TransferGroupId', None)
            self.TransferType = to_enum(TransferTypeFlag, getattr(obj, 'TransferType', None))
            self.ExternalMerchantGroupId = getattr(obj, 'ExternalMerchantGroupId', None)
            self.OnlyWithErrors = getattr(obj, 'OnlyWithErrors', None)


