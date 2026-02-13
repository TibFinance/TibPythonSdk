

from .BaseApiResponse import BaseApiResponse
from ..objects import TransactionResultEntity


class ProcessTransmissionResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.TransmissionResults = None
            self.CompressedTransmissionResults = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.TransmissionResults = []
                if hasattr(obj, 'TransmissionResults') and obj.TransmissionResults is not None:
                    self.TransmissionResults = [TransactionResultEntity(name) for name in  obj.TransmissionResults]
                self.CompressedTransmissionResults = getattr(obj, 'CompressedTransmissionResults', None)


