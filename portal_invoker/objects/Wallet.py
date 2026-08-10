
from ..utility import to_enum

from ..enums import ReferenceType
from ..enums import WalletType


class Wallet:
    def __init__(self, obj=None):
        if obj is None:
            
            self.WalletId = None
            self.ReferenceType = None
            self.ReferenceId = None
            self.Balance = None
            self.WithdrawableAmount = None
            self.WalletRefillSchedule = None
            self.IsProcessing = None
            self.WalletType = None
            self.WalletHolders = None
            self.ReferenceTypeName = None
            self.WalletTypeName = None
            self.WalletCombinationTypeName = None
            self.WalletDescription = None
            self.WalletFeatureIsActive = None

        else:
            
            from .WalletHolder import WalletHolder
            self.WalletId = getattr(obj, 'WalletId', None)
            self.ReferenceType = to_enum(ReferenceType, getattr(obj, 'ReferenceType', None))
            self.ReferenceId = getattr(obj, 'ReferenceId', None)
            self.Balance = getattr(obj, 'Balance', None)
            self.WithdrawableAmount = getattr(obj, 'WithdrawableAmount', None)
            self.WalletRefillSchedule = getattr(obj, 'WalletRefillSchedule', None)
            self.IsProcessing = getattr(obj, 'IsProcessing', None)
            self.WalletType = to_enum(WalletType, getattr(obj, 'WalletType', None))

            self.WalletHolders = []
            if hasattr(obj, 'WalletHolders') and obj.WalletHolders is not None:
                self.WalletHolders = [WalletHolder(name) for name in  obj.WalletHolders]
            self.ReferenceTypeName = getattr(obj, 'ReferenceTypeName', None)
            self.WalletTypeName = getattr(obj, 'WalletTypeName', None)
            self.WalletCombinationTypeName = getattr(obj, 'WalletCombinationTypeName', None)
            self.WalletDescription = getattr(obj, 'WalletDescription', None)
            self.WalletFeatureIsActive = getattr(obj, 'WalletFeatureIsActive', None)


