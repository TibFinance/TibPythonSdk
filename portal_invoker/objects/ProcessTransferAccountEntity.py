

from .ProcessTransferEntity import ProcessTransferEntity


class ProcessTransferAccountEntity(ProcessTransferEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.AccountInformation = None
            self.ProviderGivenIdentification = None

        else:
            super().__init__(obj)

            from .Account import Account
            self.AccountInformation = Account(getattr(obj, 'AccountInformation', None)) if getattr(obj, 'AccountInformation', None) is not None else None
            self.ProviderGivenIdentification = getattr(obj, 'ProviderGivenIdentification', None)


