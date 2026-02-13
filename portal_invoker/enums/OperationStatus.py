
import enum

class OperationStatus(enum.Enum):
    Unknown = -1
    NotSet = 0
    Success_Success = 1
    Success_NoResultReturned = 2
    Success_Skip = 3
    Success_WaitManual = 4
    Success_Error = 10
    Error_Temporary = 11
    Error_Fatal = 12
    Abort = 13

