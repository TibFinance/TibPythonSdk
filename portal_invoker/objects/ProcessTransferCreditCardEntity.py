

from .ProcessTransferEntity import ProcessTransferEntity


class ProcessTransferCreditCardEntity(ProcessTransferEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CardInformation = None
            self.NeedValidation = None
            self.ProviderGivenIdentification = None

        else:
            super().__init__(obj)

            from .CreditCard import CreditCard
            self.CardInformation = CreditCard(getattr(obj, 'CardInformation', None)) if getattr(obj, 'CardInformation', None) is not None else None
            self.NeedValidation = getattr(obj, 'NeedValidation', None)
            self.ProviderGivenIdentification = getattr(obj, 'ProviderGivenIdentification', None)


