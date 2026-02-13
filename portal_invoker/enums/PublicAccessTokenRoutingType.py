
import enum

class PublicAccessTokenRoutingType(enum.Enum):
    NotSet = 0
    Transfer = 1
    AnonymousPayment = 2
    CreateService = 3
    PendingChange = 4
    KnowCustomerPayment = 5
    DropIn = 6
    SignUp = 8
    Boarding = 9
    BoardingContract = 10
    ChangePassword = 11
    ExternalSupplierFinancialInformationsRequest = 12
    ExternalSupplierReadOnlyPortalLink = 13

