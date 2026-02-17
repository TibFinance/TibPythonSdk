
import enum

class AutorizedPaymentMethodFlags(enum.Enum):
    NotSet = 0
    CreditCard = 1
    DirectAccount = 2
    CreditCardPPA = 4
    DirectAccountPPA = 8
    Interac = 16
    CreditCardVisa = 32
    CreditCardMastercard = 64
    CreditCardAmex = 128

