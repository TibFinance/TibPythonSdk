


from ..enums import TransferType


class TransferCreation:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CreatedDate = None
            self.GroupId = None
            self.NumberOfTransfers = None
            self.TransferType = None

        else:
            
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.NumberOfTransfers = getattr(obj, 'NumberOfTransfers', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None


