
import enum

class CredentialType(enum.Enum):
    AccountCollect = 1
    PasswordCollect = 2
    AccountDeposit = 3
    PasswordDeposit = 4
    Address = 5
    KeyValuePair = 6
    Question = 7
    ProviderId = 8
    MerchantCredentials = 9

