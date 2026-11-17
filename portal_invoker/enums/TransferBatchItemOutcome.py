
import enum

class TransferBatchItemOutcome(enum.Enum):
    Created = 1
    AlreadyCreated = 2
    Refused = 3
    NotProcessed = 4
    Valid = 5
    Accepted = 6

