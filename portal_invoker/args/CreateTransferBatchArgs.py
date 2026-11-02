


from ..objects import TransferBatchItem


class CreateTransferBatchArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.IdempotencyKey = None
            self.MerchantId = None
            self.GroupId = None
            self.ValidateOnly = None
            self.Items = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.IdempotencyKey = getattr(obj, 'IdempotencyKey', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.ValidateOnly = getattr(obj, 'ValidateOnly', None)

            self.Items = []
            if hasattr(obj, 'Items') and obj.Items is not None:
                self.Items = [TransferBatchItem(name) for name in  obj.Items]


