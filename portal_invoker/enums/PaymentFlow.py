
import enum

class PaymentFlow(enum.Enum):
    Unkown = -1
    NotSet = 0
    AnonymousOnlinePayment = 1
    KnownCustomerMustUsePresavedPaymentMethod = 2
    KnownCustomerCanManagePaymentMethod = 3
    KnownCustomerCanSetAutoPaymentMethod = 4
    KnownCustomerAutoPaymentUsingPreference = 5
    KnownCustomerAutoPaymentForcePaymentMethod = 6
    AutoSelectEasier = 7
    AutoSelectEasierExceptAutoPayment = 8

