




class WalletHolder:
    def __init__(self, obj=None):
        if obj is None:
            
            self.WalletHolderId = None
            self.MerchantId = None
            self.MerchantName = None
            self.Balance = None
            self.IsProcessing = None
            self.WalletId = None
            self.DepositAmount = None

        else:
            
            self.WalletHolderId = getattr(obj, 'WalletHolderId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.Balance = getattr(obj, 'Balance', None)

            self.IsProcessing = []
            if hasattr(obj, 'IsProcessing') and obj.IsProcessing is not None:
                self.IsProcessing = [name for name in obj.IsProcessing]
            self.WalletId = getattr(obj, 'WalletId', None)
            self.DepositAmount = getattr(obj, 'DepositAmount', None)


