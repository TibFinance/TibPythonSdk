


from ..enums import Provider
from ..enums import TransferDirection


class ProviderTransactionIdentity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderType = None
            self.ProviderId = None
            self.TransferDirection = None
            self.ProviderTransactionId = None
            self.ProviderTransactionGroupId = None

        else:
            
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None
            self.ProviderId = getattr(obj, 'ProviderId', None)
            self.TransferDirection = TransferDirection(getattr(obj, 'TransferDirection', None)) if getattr(obj, 'TransferDirection', None) is not None else None
            self.ProviderTransactionId = getattr(obj, 'ProviderTransactionId', None)
            self.ProviderTransactionGroupId = getattr(obj, 'ProviderTransactionGroupId', None)


