
from ..utility import to_enum
from .BaseApiResponse import BaseApiResponse
from ..enums import TransferBatchStatus
from ..objects import TransferBatchTotals
from ..objects import TransferBatchItemResult


class GetTransferBatchResultResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BatchId = None
            self.MerchantId = None
            self.GroupId = None
            self.Status = None
            self.BatchErrorCode = None
            self.BatchMessage = None
            self.AcceptedDate = None
            self.StartedDate = None
            self.CompletedDate = None
            self.Totals = None
            self.Results = None
            self.NextIndex = None

        else:
            super().__init__(obj)
            self.BatchId = getattr(obj, 'BatchId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.Status = to_enum(TransferBatchStatus, getattr(obj, 'Status', None))
            self.BatchErrorCode = getattr(obj, 'BatchErrorCode', None)
            self.BatchMessage = getattr(obj, 'BatchMessage', None)
            self.AcceptedDate = getattr(obj, 'AcceptedDate', None)
            self.StartedDate = getattr(obj, 'StartedDate', None)
            self.CompletedDate = getattr(obj, 'CompletedDate', None)
            self.Totals = TransferBatchTotals(getattr(obj, 'Totals', None)) if getattr(obj, 'Totals', None) is not None else None

            self.Results = []
            if hasattr(obj, 'Results') and obj.Results is not None:
                self.Results = [TransferBatchItemResult(name) for name in  obj.Results]
            self.NextIndex = getattr(obj, 'NextIndex', None)


