

from .ProcessTransferEntity import ProcessTransferEntity


class ProcessTransferInteracEntity(ProcessTransferEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.InteracInformation = None
            self.AnswerSalt = None
            self.MerchantEmail = None

        else:
            super().__init__(obj)

            from .Interac import Interac
            self.InteracInformation = Interac(getattr(obj, 'InteracInformation', None)) if getattr(obj, 'InteracInformation', None) is not None else None
            self.AnswerSalt = getattr(obj, 'AnswerSalt', None)
            self.MerchantEmail = getattr(obj, 'MerchantEmail', None)


