
import enum

class BoardingStep(enum.Enum):
    CompanyInfoRejected = -2
    Unkown = -1
    NotSet = 0
    ClientCreated = 1
    LoginCreated = 2
    CompanyInfoToValidate = 3
    CompanyInfoValidated = 4

