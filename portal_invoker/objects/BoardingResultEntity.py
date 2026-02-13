

from .BoardingBaseResult import BoardingBaseResult


class BoardingResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ProviderRequestId = None
            self.Processing = None

        else:
            super().__init__(obj)

            self.ProviderRequestId = getattr(obj, 'ProviderRequestId', None)
            self.Processing = getattr(obj, 'Processing', None)


