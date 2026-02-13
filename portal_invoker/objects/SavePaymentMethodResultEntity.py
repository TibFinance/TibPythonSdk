

from .BoardingBaseResult import BoardingBaseResult


class SavePaymentMethodResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderGivenIdentification = None

        else:
            super().__init__(obj)

            self.ProviderGivenIdentification = getattr(obj, 'ProviderGivenIdentification', None)


