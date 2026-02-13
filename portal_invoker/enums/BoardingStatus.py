
import enum

class BoardingStatus(enum.Enum):
    NotSet = 0
    Draft = 1
    Submit = 11
    InReview = 12
    Completed = 13
    ValidationError = 21
    DocumentsRequired = 22
    Rejected = 23
    DocumentsSubmitted = 24

