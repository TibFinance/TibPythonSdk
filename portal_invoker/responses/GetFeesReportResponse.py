

from .BaseApiResponse import BaseApiResponse
from ..objects import FeeReportLineItem
from ..objects import FeeSummary


class GetFeesReportResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.FeeItems = None
            self.Summary = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.FeeItems = []
                if hasattr(obj, 'FeeItems') and obj.FeeItems is not None:
                    self.FeeItems = [FeeReportLineItem(name) for name in  obj.FeeItems]
                self.Summary = FeeSummary(getattr(obj, 'Summary', None)) if getattr(obj, 'Summary', None) is not None else None


