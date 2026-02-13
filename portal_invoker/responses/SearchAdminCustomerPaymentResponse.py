

from .BaseApiResponse import BaseApiResponse
from ..objects import AdminCustomerPayment


class SearchAdminCustomerPaymentResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.SearchResult = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.SearchResult = []
                if hasattr(obj, 'SearchResult') and obj.SearchResult is not None:
                    self.SearchResult = [AdminCustomerPayment(name) for name in  obj.SearchResult]


