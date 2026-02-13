
import enum

class BankingOperationResult(enum.Enum):
    Unknown = -1
    NotSet = 0
    Confirmed = 1
    ErrorOther = 2
    NoFund = 3
    AccountError = 4
    Opposition = 5
    InteracRefused = 6
    InteracFailed = 7

