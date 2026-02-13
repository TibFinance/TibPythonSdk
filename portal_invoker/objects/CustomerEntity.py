


from ..enums import Language


class CustomerEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerName = None
            self.CustomerExternalId = None
            self.Language = None
            self.CustomerDescription = None
            self.CustomerEmail = None
            self.PaymentMethods = None
            self.ContactInfo = None

        else:
            
            from .PaymentMethod import PaymentMethod
            from .ContactInfo import ContactInfo
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CustomerExternalId = getattr(obj, 'CustomerExternalId', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.CustomerDescription = getattr(obj, 'CustomerDescription', None)
            self.CustomerEmail = getattr(obj, 'CustomerEmail', None)

            self.PaymentMethods = []
            if hasattr(obj, 'PaymentMethods') and obj.PaymentMethods is not None:
                self.PaymentMethods = [PaymentMethod(name) for name in  obj.PaymentMethods]
            self.ContactInfo = ContactInfo(getattr(obj, 'ContactInfo', None)) if getattr(obj, 'ContactInfo', None) is not None else None


