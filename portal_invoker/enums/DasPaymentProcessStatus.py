
import enum

class DasPaymentProcessStatus(enum.Enum):
    NotSet = 0
    New = 1
    MoneyCollected = 2
    ReadyToSend = 3
    PaymentSent = 4
    PaymentAccepted = 5
    Cancelled = 10
    Reverted = 11
    ErrorCollectingMoney = 100
    ErrorPreparingPayment = 101
    ErrorSendingPayment = 102

