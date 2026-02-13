
import enum

class CheckFeesMode(enum.Enum):
    Unknown = -1
    FeesOnEachCall = 0
    FeesOnEachCallOnlyFound = 1
    OncePerMonth = 2
    OncePerMonthOnlyIfFound = 3
    NoFees = 4

