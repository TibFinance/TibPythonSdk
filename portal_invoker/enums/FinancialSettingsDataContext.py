
import enum

class FinancialSettingsDataContext(enum.Enum):
    NotSet = 0
    DefaultClientSettings = 1
    DefaultClientServiceSettings = 2
    ClientSettings = 3
    ClientDefaultServiceSettings = 4
    ServiceSettings = 5
    MerchantSettings = 6

