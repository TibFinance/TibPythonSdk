

from .BaseApiResponse import BaseApiResponse
from ..objects import ErrorReportData


class ErrorReportDataResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ErrorReportDataList = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.ErrorReportDataList = []
                if hasattr(obj, 'ErrorReportDataList') and obj.ErrorReportDataList is not None:
                    self.ErrorReportDataList = [ErrorReportData(name) for name in  obj.ErrorReportDataList]


