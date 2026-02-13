




class SearchAdminArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.SearchText = None
            self.ClientId = None
            self.DateFrom = None
            self.DateTo = None
            self.MerchantIds = None
            self.CustomerIds = None
            self.TransferIds = None
            self.OperationIds = None
            self.TransactionGroupIds = None
            self.TransactionIds = None
            self.TransferType = None
            self.TIBAuthorizationStatus = None
            self.OperationTarget = None
            self.OperationDirection = None
            self.OperationKind = None
            self.OperationStatus = None
            self.OperationType = None
            self.RowCount = None
            self.IsTextSearch = None
            self.IsRevertSearch = None
            self.DueDateFrom = None
            self.DueDateTo = None
            self.ExecutedFrom = None
            self.ExecutedTo = None
            self.RealDueDateFrom = None
            self.RealDueDateTo = None
            self.LastModifiedDateFrom = None
            self.LastModifiedDateTo = None
            self.IsCreatedDateChecked = None
            self.IsDueDateChecked = None
            self.IsExecutedDateChecked = None
            self.IsRealDueDateChecked = None
            self.IsLastModifiedDateChecked = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.SearchText = getattr(obj, 'SearchText', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.DateFrom = getattr(obj, 'DateFrom', None)
            self.DateTo = getattr(obj, 'DateTo', None)

            self.MerchantIds = []
            if hasattr(obj, 'MerchantIds') and obj.MerchantIds is not None:
                self.MerchantIds = [name for name in obj.MerchantIds]

            self.CustomerIds = []
            if hasattr(obj, 'CustomerIds') and obj.CustomerIds is not None:
                self.CustomerIds = [name for name in obj.CustomerIds]

            self.TransferIds = []
            if hasattr(obj, 'TransferIds') and obj.TransferIds is not None:
                self.TransferIds = [name for name in obj.TransferIds]

            self.OperationIds = []
            if hasattr(obj, 'OperationIds') and obj.OperationIds is not None:
                self.OperationIds = [name for name in obj.OperationIds]

            self.TransactionGroupIds = []
            if hasattr(obj, 'TransactionGroupIds') and obj.TransactionGroupIds is not None:
                self.TransactionGroupIds = [name for name in obj.TransactionGroupIds]

            self.TransactionIds = []
            if hasattr(obj, 'TransactionIds') and obj.TransactionIds is not None:
                self.TransactionIds = [name for name in obj.TransactionIds]
            self.TransferType = getattr(obj, 'TransferType', None)
            self.TIBAuthorizationStatus = getattr(obj, 'TIBAuthorizationStatus', None)
            self.OperationTarget = getattr(obj, 'OperationTarget', None)
            self.OperationDirection = getattr(obj, 'OperationDirection', None)
            self.OperationKind = getattr(obj, 'OperationKind', None)
            self.OperationStatus = getattr(obj, 'OperationStatus', None)
            self.OperationType = getattr(obj, 'OperationType', None)
            self.RowCount = getattr(obj, 'RowCount', None)
            self.IsTextSearch = getattr(obj, 'IsTextSearch', None)
            self.IsRevertSearch = getattr(obj, 'IsRevertSearch', None)
            self.DueDateFrom = getattr(obj, 'DueDateFrom', None)
            self.DueDateTo = getattr(obj, 'DueDateTo', None)
            self.ExecutedFrom = getattr(obj, 'ExecutedFrom', None)
            self.ExecutedTo = getattr(obj, 'ExecutedTo', None)
            self.RealDueDateFrom = getattr(obj, 'RealDueDateFrom', None)
            self.RealDueDateTo = getattr(obj, 'RealDueDateTo', None)
            self.LastModifiedDateFrom = getattr(obj, 'LastModifiedDateFrom', None)
            self.LastModifiedDateTo = getattr(obj, 'LastModifiedDateTo', None)
            self.IsCreatedDateChecked = getattr(obj, 'IsCreatedDateChecked', None)
            self.IsDueDateChecked = getattr(obj, 'IsDueDateChecked', None)
            self.IsExecutedDateChecked = getattr(obj, 'IsExecutedDateChecked', None)
            self.IsRealDueDateChecked = getattr(obj, 'IsRealDueDateChecked', None)
            self.IsLastModifiedDateChecked = getattr(obj, 'IsLastModifiedDateChecked', None)


