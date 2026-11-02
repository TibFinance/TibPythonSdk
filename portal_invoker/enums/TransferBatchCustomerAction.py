
import enum

class TransferBatchCustomerAction(enum.Enum):
    NotSet = 0
    Created = 1
    Updated = 2
    Unchanged = 3
    Recreated = 4
    NotStored = 5

