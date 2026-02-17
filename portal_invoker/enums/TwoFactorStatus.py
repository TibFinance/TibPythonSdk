
import enum

class TwoFactorStatus(enum.Enum):
    NotRequired = 0
    CodeRequired = 1
    SetupRequired = 2
    Verified = 3
    InvalidCode = 4
    SecurityVerificationRequired = 5
    SecurityVerificationFailed = 6
    SecurityVerificationUnavailable = 7

