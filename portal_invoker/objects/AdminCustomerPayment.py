


from ..enums import PaymentMethodType
from ..enums import Language


class AdminCustomerPayment:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CustomerId = None
            self.ServiceId = None
            self.PaymentMethodId = None
            self.AccountInformationId = None
            self.CustomerName = None
            self.CustomerEmail = None
            self.Description = None
            self.AccountInformationView = None
            self.PaymentMethodType = None
            self.Owner = None
            self.ExternalCustomerId = None
            self.IsDeletedCustomer = None
            self.PaymentMethodDescription = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.IsVerifiedPaymentMethod = None
            self.IsDeletedPaymentMethod = None
            self.ExpirationDate = None
            self.AccountAddressId = None
            self.Question = None
            self.Email = None
            self.MobilePhone = None
            self.AccountLanguage = None
            self.Memo = None
            self.IsChecked = None
            self.CreatedDateCustomer = None
            self.CreatedDatePaymentMethod = None
            self.CustomerInfoEmail = None
            self.Phone = None
            self.Address = None
            self.City = None
            self.PostalZipCode = None
            self.PaymentMethodTypeValue = None
            self.AccountLanguageValue = None

        else:
            
            self.CustomerId = getattr(obj, 'CustomerId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.AccountInformationId = getattr(obj, 'AccountInformationId', None)
            self.CustomerName = getattr(obj, 'CustomerName', None)
            self.CustomerEmail = getattr(obj, 'CustomerEmail', None)
            self.Description = getattr(obj, 'Description', None)
            self.AccountInformationView = getattr(obj, 'AccountInformationView', None)
            self.PaymentMethodType = PaymentMethodType(getattr(obj, 'PaymentMethodType', None)) if getattr(obj, 'PaymentMethodType', None) is not None else None
            self.Owner = getattr(obj, 'Owner', None)
            self.ExternalCustomerId = getattr(obj, 'ExternalCustomerId', None)
            self.IsDeletedCustomer = getattr(obj, 'IsDeletedCustomer', None)
            self.PaymentMethodDescription = getattr(obj, 'PaymentMethodDescription', None)
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.IsVerifiedPaymentMethod = getattr(obj, 'IsVerifiedPaymentMethod', None)
            self.IsDeletedPaymentMethod = getattr(obj, 'IsDeletedPaymentMethod', None)
            self.ExpirationDate = getattr(obj, 'ExpirationDate', None)
            self.AccountAddressId = getattr(obj, 'AccountAddressId', None)
            self.Question = getattr(obj, 'Question', None)
            self.Email = getattr(obj, 'Email', None)
            self.MobilePhone = getattr(obj, 'MobilePhone', None)
            self.AccountLanguage = Language(getattr(obj, 'AccountLanguage', None)) if getattr(obj, 'AccountLanguage', None) is not None else None
            self.Memo = getattr(obj, 'Memo', None)
            self.IsChecked = getattr(obj, 'IsChecked', None)
            self.CreatedDateCustomer = getattr(obj, 'CreatedDateCustomer', None)
            self.CreatedDatePaymentMethod = getattr(obj, 'CreatedDatePaymentMethod', None)
            self.CustomerInfoEmail = getattr(obj, 'CustomerInfoEmail', None)
            self.Phone = getattr(obj, 'Phone', None)
            self.Address = getattr(obj, 'Address', None)
            self.City = getattr(obj, 'City', None)
            self.PostalZipCode = getattr(obj, 'PostalZipCode', None)
            self.PaymentMethodTypeValue = getattr(obj, 'PaymentMethodTypeValue', None)
            self.AccountLanguageValue = getattr(obj, 'AccountLanguageValue', None)


