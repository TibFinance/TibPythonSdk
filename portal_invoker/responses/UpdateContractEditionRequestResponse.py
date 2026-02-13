

from .BaseApiResponse import BaseApiResponse
from ..objects import ContractEditionRequest


class UpdateContractEditionRequestResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ContractEditionRequest = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.ContractEditionRequest = ContractEditionRequest(getattr(obj, 'ContractEditionRequest', None)) if getattr(obj, 'ContractEditionRequest', None) is not None else None


