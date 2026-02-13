

from .BoardingBaseResult import BoardingBaseResult


class GetBlueSnapClientTokenResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Token = None

        else:
            super().__init__(obj)

            self.Token = getattr(obj, 'Token', None)


