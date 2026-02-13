
import enum

class ClientAuthorizationStatus(enum.Enum):
    NotRequired = 0
    NeedApprobation = 1
    Approved = 2
    Rejected = 3

