
import enum

class TibAuthorizationStatus(enum.Enum):
    NotRequired = 0
    WaitingForClientApprobation = 1
    Required = 2
    Approved = 3
    Declined = 4

