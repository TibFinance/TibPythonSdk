
import enum

class EventToBroadcastType(enum.Enum):
    NotSet = 0
    TransactionEventToBroadcast = 1
    BatchFileEventToBroadcast = 2
    BoardingEventToBroadcast = 3
    TransferPendingProcessEventToBroadcast = 4

