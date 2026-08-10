
from ..utility import to_enum

from ..enums import TransferType


class ListTransfersFastArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.FromDate = None
            self.ToDate = None
            self.ServiceId = None
            self.MerchantId = None
            self.TransferGroupId = None
            self.TransferType = None
            self.MarkResolvedOnly = None
            self.ExternalMerchantGroupId = None
            self.OnlyWithErrors = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.FromDate = getattr(obj, 'FromDate', None)
            self.ToDate = getattr(obj, 'ToDate', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.TransferGroupId = getattr(obj, 'TransferGroupId', None)
            self.TransferType = to_enum(TransferType, getattr(obj, 'TransferType', None))
            self.MarkResolvedOnly = getattr(obj, 'MarkResolvedOnly', None)
            self.ExternalMerchantGroupId = getattr(obj, 'ExternalMerchantGroupId', None)
            self.OnlyWithErrors = getattr(obj, 'OnlyWithErrors', None)


