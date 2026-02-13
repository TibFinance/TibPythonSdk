

from .ProviderEntity import ProviderEntity
from ..enums import PaymentMethodType
from ..enums import OwnerType
from ..enums import Currency


class ProviderAccount(ProviderEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.CredentialValuesTypes = None
            self.ProviderName = None
            self.PaymentMethodType = None
            self.IsDefault = None
            self.OwnerType = None
            self.Currency = None

        else:
            super().__init__(obj)

            from .CredentialValueType import CredentialValueType

            self.CredentialValuesTypes = []
            if hasattr(obj, 'CredentialValuesTypes') and obj.CredentialValuesTypes is not None:
                self.CredentialValuesTypes = [CredentialValueType(name) for name in  obj.CredentialValuesTypes]
            self.ProviderName = getattr(obj, 'ProviderName', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.IsDefault = getattr(obj, 'IsDefault', None)
            self.OwnerType = OwnerType(getattr(obj, 'OwnerType', None)) if getattr(obj, 'OwnerType', None) is not None else None
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None


