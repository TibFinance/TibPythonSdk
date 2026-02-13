

from .BoardingBaseResult import BoardingBaseResult


class SubmitDocumentResultEntity(BoardingBaseResult):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Status = None

        else:
            super().__init__(obj)

            self.Status = getattr(obj, 'Status', None)


