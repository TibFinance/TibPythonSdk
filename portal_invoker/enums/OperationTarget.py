
import enum

class OperationTarget(enum.Enum):
    Unknown = -1
    NotSet = 0
    Client = 1
    Merchant = 2
    TibClient = 3
    Wallet = 4
    Tib = 100

