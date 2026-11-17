
import enum

class TransferBatchOutcome(enum.Enum):
    Processed = 1
    Refused = 2
    Validated = 3
    Accepted = 4

