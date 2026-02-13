

from .BaseApiResponse import BaseApiResponse
from ..objects import OperationDateReportEntity
from ..objects import TransferBaseInformationEntity
from ..objects import USOperationReportEntity


class GetOperationsReportResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.DateLineReport = None
            self.Transfers = None
            self.USOperationsData = None
            self.IsBrandNewSupplier = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.DateLineReport = []
                if hasattr(obj, 'DateLineReport') and obj.DateLineReport is not None:
                    self.DateLineReport = [OperationDateReportEntity(name) for name in  obj.DateLineReport]

                self.Transfers = []
                if hasattr(obj, 'Transfers') and obj.Transfers is not None:
                    self.Transfers = [TransferBaseInformationEntity(name) for name in  obj.Transfers]

                self.USOperationsData = []
                if hasattr(obj, 'USOperationsData') and obj.USOperationsData is not None:
                    self.USOperationsData = [USOperationReportEntity(name) for name in  obj.USOperationsData]
                self.IsBrandNewSupplier = getattr(obj, 'IsBrandNewSupplier', None)


