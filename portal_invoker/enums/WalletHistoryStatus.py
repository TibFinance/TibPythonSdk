
import enum

class WalletHistoryStatus(enum.Enum):
    NotSet = 0
    New = 1
    InProgress = 2
    Failed = 3
    Abord = 4
    Success = 5
    Lost = 6

