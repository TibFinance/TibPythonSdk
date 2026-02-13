

from .BaseApiResponse import BaseApiResponse
from ..objects import ContractEditionRequest


class GetContractEditionRequestsResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ContractEdditionRequests = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.ContractEdditionRequests = []
                if hasattr(obj, 'ContractEdditionRequests') and obj.ContractEdditionRequests is not None:
                    self.ContractEdditionRequests = [ContractEditionRequest(name) for name in  obj.ContractEdditionRequests]


