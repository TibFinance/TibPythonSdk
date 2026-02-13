
import enum

class ValidationLimitStatus(enum.Enum):
    NoErrors = 0
    LimitPerBankAccountDailyReach = 1
    LimitPerBankAccountPerDelaysReach = 2
    NumberPerBankAccountDailyReach = 4
    NumberPerBankAccountPerDelaysReach = 8
    LimitReach = 16
    LimitDailyReach = 32
    LimitClientDailyReach = 64

