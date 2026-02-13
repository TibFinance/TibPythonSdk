




class TransferPayload:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransferId = None
            self.Amount = None
            self.OperationKind = None
            self.OriginalAmount = None
            self.ExternalReferenceId = None
            self.DueDate = None
            self.CreatedDate = None
            self.PaymentMethodId = None
            self.PaymentMethodDescription = None
            self.PaymentMethodPreview = None
            self.CustomerId = None
            self.CustomerName = None
            self.CustomerExternalId = None
            self.BillAmount = None
            self.BillCurrency = None
            self.BillDescription = None
            self.BillId = None
            self.BillLanguage = None
            self.BillTitle = None
            self.BillCreatedDate = None
            self.ExternalSystemBillNumber1 = None
            self.ExternalSystemBillNumber2 = None
            self.ExternalSystemBillNumber3 = None
            self.BillMerchantId = None
            self.BillCustomerId = None
            self.Payout = None

        else:
            
            from .PayoutPayload import PayoutPayload
            self.TransferId = getattr(obj, 'TransferId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.OperationKind = getattr(obj, 'OperationKind', None)
            self.OriginalAmount = getattr(obj, 'OriginalAmount', None)
            self.ExternalReferenceId = getattr(obj, 'ExternalReferenceId', None)
            self.DueDate = getattr(obj, 'DueDate', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.PaymentMethodDescription = getattr(obj, 'PaymentMethodDescription', None)
            self.PaymentMethodPreview = getattr(obj, 'PaymentMethodPreview', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CustomerExternalId = getattr(obj, 'CustomerExternalId', None)
            self.BillAmount = getattr(obj, 'BillAmount', None)
            self.BillCurrency = getattr(obj, 'BillCurrency', None)
            self.BillDescription = getattr(obj, 'BillDescription', None)
            self.BillId = getattr(obj, 'BillId', None)
            self.BillLanguage = getattr(obj, 'BillLanguage', None)
            self.BillTitle = getattr(obj, 'BillTitle', None)
            self.BillCreatedDate = getattr(obj, 'BillCreatedDate', None)
            self.ExternalSystemBillNumber1 = getattr(obj, 'ExternalSystemBillNumber1', None)
            self.ExternalSystemBillNumber2 = getattr(obj, 'ExternalSystemBillNumber2', None)
            self.ExternalSystemBillNumber3 = getattr(obj, 'ExternalSystemBillNumber3', None)
            self.BillMerchantId = getattr(obj, 'BillMerchantId', None)
            self.BillCustomerId = getattr(obj, 'BillCustomerId', None)
            self.Payout = PayoutPayload(getattr(obj, 'Payout', None)) if getattr(obj, 'Payout', None) is not None else None


