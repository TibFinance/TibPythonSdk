


from ..enums import PaymentMethodType
from ..enums import Currency
from ..enums import Provider
from ..enums import OwnerType


class ProviderAccountDecrypted:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProviderId = None
            self.ProviderName = None
            self.OrderPriority = None
            self.IsDefault = None
            self.PaymentMethodType = None
            self.Currency = None
            self.ProviderType = None
            self.OwnerType = None
            self.AccountCollect = None
            self.AccountDeposit = None
            self.PasswordCollect = None
            self.PasswordDeposit = None
            self.Questions = None
            self.Addresses = None
            self.CredentialValues = None
            self.ProviderOtherCredentialValues = None
            self.MerchantCredentialValues = None

        else:
            
            from .QuestionAnswerDecrypted import QuestionAnswerDecrypted
            from .ProviderAddressEntity import ProviderAddressEntity
            from .ProviderMerchantCredentialEntity import ProviderMerchantCredentialEntity
            self.ProviderId = getattr(obj, 'ProviderId', None)
            self.ProviderName = getattr(obj, 'ProviderName', None)
            self.OrderPriority = getattr(obj, 'OrderPriority', None)
            self.IsDefault = getattr(obj, 'IsDefault', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.ProviderType = Provider(getattr(obj, 'ProviderType', None)) if getattr(obj, 'ProviderType', None) is not None else None
            self.OwnerType = OwnerType(getattr(obj, 'OwnerType', None)) if getattr(obj, 'OwnerType', None) is not None else None
            self.AccountCollect = getattr(obj, 'AccountCollect', None)
            self.AccountDeposit = getattr(obj, 'AccountDeposit', None)
            self.PasswordCollect = getattr(obj, 'PasswordCollect', None)
            self.PasswordDeposit = getattr(obj, 'PasswordDeposit', None)

            self.Questions = []
            if hasattr(obj, 'Questions') and obj.Questions is not None:
                self.Questions = [QuestionAnswerDecrypted(name) for name in  obj.Questions]

            self.Addresses = []
            if hasattr(obj, 'Addresses') and obj.Addresses is not None:
                self.Addresses = [ProviderAddressEntity(name) for name in  obj.Addresses]

            self.CredentialValues = []
            if hasattr(obj, 'CredentialValues') and obj.CredentialValues is not None:
                self.CredentialValues = [name for name in obj.CredentialValues]

            self.ProviderOtherCredentialValues = []
            if hasattr(obj, 'ProviderOtherCredentialValues') and obj.ProviderOtherCredentialValues is not None:
                self.ProviderOtherCredentialValues = [name for name in obj.ProviderOtherCredentialValues]

            self.MerchantCredentialValues = []
            if hasattr(obj, 'MerchantCredentialValues') and obj.MerchantCredentialValues is not None:
                self.MerchantCredentialValues = [ProviderMerchantCredentialEntity(name) for name in  obj.MerchantCredentialValues]


