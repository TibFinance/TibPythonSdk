


from ..objects import Interac
from ..enums import Language


class CreateInteracPaymentMethodArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.CustomerId = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.InteracInformation = None
            self.Language = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.InteracInformation = Interac(getattr(obj, 'InteracInformation', None)) if getattr(obj, 'InteracInformation', None) is not None else None
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.MerchantId = getattr(obj, 'MerchantId', None)


