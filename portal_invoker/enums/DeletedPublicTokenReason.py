
import enum

class DeletedPublicTokenReason(enum.Enum):
    NotSet = 0
    Consumed = 1
    Expired = 2
    Canceled = 3
    WeSentYouNewLogin = 9

