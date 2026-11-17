




class TransferBatchTotals:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ItemCount = None
            self.CreatedCount = None
            self.AlreadyCreatedCount = None
            self.RefusedCount = None
            self.NotProcessedCount = None
            self.AcceptedCount = None
            self.CreatedCollectionAmount = None
            self.CreatedDepositAmount = None

        else:
            
            self.ItemCount = getattr(obj, 'ItemCount', None)
            self.CreatedCount = getattr(obj, 'CreatedCount', None)
            self.AlreadyCreatedCount = getattr(obj, 'AlreadyCreatedCount', None)
            self.RefusedCount = getattr(obj, 'RefusedCount', None)
            self.NotProcessedCount = getattr(obj, 'NotProcessedCount', None)
            self.AcceptedCount = getattr(obj, 'AcceptedCount', None)
            self.CreatedCollectionAmount = getattr(obj, 'CreatedCollectionAmount', None)
            self.CreatedDepositAmount = getattr(obj, 'CreatedDepositAmount', None)


