

from .BaseApiResponse import BaseApiResponse
from ..objects import ContractInfoEntity
from ..objects import EditionRequest


class LoadContractCompanyInfosResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CompanyInfos = None
            self.EditionRequests = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.CompanyInfos = ContractInfoEntity(getattr(obj, 'CompanyInfos', None)) if getattr(obj, 'CompanyInfos', None) is not None else None

                self.EditionRequests = []
                if hasattr(obj, 'EditionRequests') and obj.EditionRequests is not None:
                    self.EditionRequests = [EditionRequest(name) for name in  obj.EditionRequests]


