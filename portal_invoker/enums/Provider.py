
import enum

class Provider(enum.Enum):
    Unknown = -1
    NotSet = 0
    CA_CreditCard_Moneris = 1000
    CA_CreditCard_BankOfAmerica = 1001
    CA_Account_Desjardins = 1100
    CA_Account_RBC = 1101
    CA_Interac_RBC = 1200
    RBC_ARN = 3000

