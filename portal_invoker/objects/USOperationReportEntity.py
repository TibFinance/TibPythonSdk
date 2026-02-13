




class USOperationReportEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Payout = None
            self.Transfers = None

        else:
            
            from .PayoutData import PayoutData
            from .TransferBaseInformationEntity import TransferBaseInformationEntity
            self.Payout = PayoutData(getattr(obj, 'Payout', None)) if getattr(obj, 'Payout', None) is not None else None

            self.Transfers = []
            if hasattr(obj, 'Transfers') and obj.Transfers is not None:
                self.Transfers = [TransferBaseInformationEntity(name) for name in  obj.Transfers]


