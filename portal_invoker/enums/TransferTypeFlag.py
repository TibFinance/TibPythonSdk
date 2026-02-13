
import enum

class TransferTypeFlag(enum.Enum):
    NotSet = 0
    Payment = 1
    FreeCollection = 2
    PaymentAndFreeCollection = 3
    FreeDeposit = 4
    PaymentAndFreeDeposit = 5
    FreeCollectionAndFreeDeposit = 6
    All = 7

