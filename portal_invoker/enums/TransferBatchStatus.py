
import enum

class TransferBatchStatus(enum.Enum):
    NotSet = 0
    Queued = 1
    Processing = 2
    Completed = 3
    Stopped = 4
    Failed = 5

