
import enum

class TibCustomPaymentStatus(enum.Enum):
    Pending = 0
    InProgress = 1
    RevertedPending = 2
    Completed = 3
    RevertedCompleted = 4
    Error = 5
    Canceled = 6

