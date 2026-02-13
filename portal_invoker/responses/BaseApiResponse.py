from ..utility import object2dict


class BaseApiResponse:
    def __init__(self, obj=None):
        if obj is None:
            
            self.HasError = None
            self.Messages = None
        else:
            self.Errors = []
            if isinstance(obj.Errors, list):
                for i in obj.Errors:
                    self.Errors.append(object2dict(i))
            self.HasError = obj.HasError
            self.Messages = obj.Messages
