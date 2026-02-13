


from ..enums import OperationKind


class ConsolidationInternalReportEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ExecutedDate = None
            self.GroupId = None
            self.OperationKind = None
            self.DepositAmount = None
            self.CollectionAmount = None
            self.ReturnedDepositAmount = None
            self.ReturnedCollectionAmount = None
            self.TransactionCount = None

        else:
            
            self.ExecutedDate = getattr(obj, 'ExecutedDate', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.OperationKind = OperationKind(getattr(obj, 'OperationKind', None)) if getattr(obj, 'OperationKind', None) is not None else None
            self.DepositAmount = getattr(obj, 'DepositAmount', None)
            self.CollectionAmount = getattr(obj, 'CollectionAmount', None)
            self.ReturnedDepositAmount = getattr(obj, 'ReturnedDepositAmount', None)
            self.ReturnedCollectionAmount = getattr(obj, 'ReturnedCollectionAmount', None)
            self.TransactionCount = getattr(obj, 'TransactionCount', None)


