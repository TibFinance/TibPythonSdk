
import enum

class PaymentFlowParsingResult(enum.Enum):
    Unkown = -1
    NoError = 0
    Success = 1
    InvalidPaymentFlow = 2
    BillNotRelatedToKnownCustomer = 3
    BillKnownCustomerHasNoPaymentMethod = 4
    BillKnownCustomerHasNoAutoPaymentSet = 5
    ForcedPaymentMethodIdNeeded = 6
    BillKnownCustomerDoesntHaveSpecifiedPaymentMethodId = 7
    AnonymousMustHaveEmail = 8
    CustomerPPAConsentIsNeeded = 9

