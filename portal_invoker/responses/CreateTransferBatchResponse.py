
from ..utility import to_enum
from .BaseApiResponse import BaseApiResponse
from ..enums import TransferBatchOutcome
from ..objects import TransferBatchTotals
from ..objects import TransferBatchItemResult


class CreateTransferBatchResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.BatchId = None
            self.BatchOutcome = None
            self.BatchErrorCode = None
            self.BatchMessage = None
            self.Totals = None
            self.Results = None

        else:
            super().__init__(obj)
            self.BatchId = getattr(obj, 'BatchId', None)
            self.BatchOutcome = to_enum(TransferBatchOutcome, getattr(obj, 'BatchOutcome', None))
            self.BatchErrorCode = getattr(obj, 'BatchErrorCode', None)
            self.BatchMessage = getattr(obj, 'BatchMessage', None)
            self.Totals = TransferBatchTotals(getattr(obj, 'Totals', None)) if getattr(obj, 'Totals', None) is not None else None

            self.Results = []
            if hasattr(obj, 'Results') and obj.Results is not None:
                self.Results = [TransferBatchItemResult(name) for name in  obj.Results]


