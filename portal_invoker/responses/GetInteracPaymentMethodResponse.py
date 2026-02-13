

from .BaseApiResponse import BaseApiResponse


class GetInteracPaymentMethodResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Question = None
            self.Owner = None
            self.Email = None
            self.Description = None
            self.Mobile = None

        else:
            super().__init__(obj)
            if not obj.HasError:
                self.Question = getattr(obj, 'Question', None)
                self.Owner = getattr(obj, 'Owner', None)
                self.Email = getattr(obj, 'Email', None)
                self.Description = getattr(obj, 'Description', None)
                self.Mobile = getattr(obj, 'Mobile', None)


