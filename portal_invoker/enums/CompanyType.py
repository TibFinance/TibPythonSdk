
import enum

class CompanyType(enum.Enum):
    Unkown = -1
    NotSet = 0
    JointStockCompany = 1
    LimitedCompany = 2
    Partnership = 3
    PublicCompany = 4
    PublicAdministration = 5
    NonprofitOrganization = 6
    SoleProprietorship = 7

