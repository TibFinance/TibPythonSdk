
import enum

class FeeMode(enum.Enum):
    Unknown = -1
    NotSet = 0
    Fix = 1
    RelativeToPaymentTypeFee = 2
    FixUsingRoundUp = 3

