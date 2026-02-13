
import enum

class OperationType(enum.Enum):
    Unknown = -1
    NotSet = 0
    Validation = 1
    Transmission = 2
    StatusCheck = 3
    Payback = 4

