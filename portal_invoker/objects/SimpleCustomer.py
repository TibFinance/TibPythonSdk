


from ..enums import Language


class SimpleCustomer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerName = None
            self.CustomerExternalId = None
            self.Language = None
            self.CustomerDescription = None
            self.CustomerEmail = None

        else:
            
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CustomerExternalId = getattr(obj, 'CustomerExternalId', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.CustomerDescription = getattr(obj, 'CustomerDescription', None)
            self.CustomerEmail = getattr(obj, 'CustomerEmail', None)


