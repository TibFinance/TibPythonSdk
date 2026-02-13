


from ..enums import TransferType
from ..enums import OperationTarget
from ..enums import OperationCategoryReportType


class GetOperationsReportArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.ServiceId = None
            self.DateFrom = None
            self.DateTo = None
            self.TransferType = None
            self.TargetType = None
            self.ReturnTransferList = None
            self.LimitToSpecificCategory = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.DateFrom = getattr(obj, 'DateFrom', None)
            self.DateTo = getattr(obj, 'DateTo', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.TargetType = OperationTarget(getattr(obj, 'TargetType', None)) if getattr(obj, 'TargetType', None) is not None else None
            self.ReturnTransferList = getattr(obj, 'ReturnTransferList', None)
            self.LimitToSpecificCategory = OperationCategoryReportType(getattr(obj, 'LimitToSpecificCategory', None)) if getattr(obj, 'LimitToSpecificCategory', None) is not None else None


