
import enum

class OperationCategoryReportType(enum.Enum):
    Deposit = 0
    Collection = 1
    Transmitted = 2
    Bill = 3
    CancelFast = 4
    CancelLate = 5
    Payback = 6
    Transaction = 7
    UserCanceled = 8

