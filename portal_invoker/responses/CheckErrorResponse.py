

from .BaseApiResponse import BaseApiResponse
from ..objects import CheckResult
from ..objects import CheckResultDetail


class CheckErrorResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CheckResult = None
            self.Result = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.CheckResult = CheckResult(obj.CheckResult)

                self.Result = []
                if hasattr(obj, 'Result') and obj.Result is not None:
                    self.Result = [CheckResultDetail(name) for name in  obj.Result]


