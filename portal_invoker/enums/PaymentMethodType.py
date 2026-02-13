
import enum

class PaymentMethodType(enum.Enum):
    Unknown = -1
    NotSet = 0
    CreditCard = 1
    DirectAccount = 2
    Interac = 3

