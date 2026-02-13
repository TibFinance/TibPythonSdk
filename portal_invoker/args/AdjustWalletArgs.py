


from ..enums import WalletAdjustment


class AdjustWalletArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceId = None
            self.MerchantId = None
            self.Amount = None
            self.Mode = None
            self.UseInterac = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Amount = getattr(obj, 'Amount', None)
            self.Mode = WalletAdjustment(getattr(obj, 'Mode', None)) if getattr(obj, 'Mode', None) is not None else None
            self.UseInterac = getattr(obj, 'UseInterac', None)


