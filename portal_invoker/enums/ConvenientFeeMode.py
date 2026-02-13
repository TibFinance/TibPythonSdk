
import enum

class ConvenientFeeMode(enum.Enum):
    Unknown = -1
    NotSet = 0
    NoFeeAuthorized = 1
    FeeWithRoundupOnPercentage = 2
    FeeWithRoundupOnAbsolute = 3
    RelativeToPaymentTypeFee = 4

