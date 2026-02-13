


from ..enums import ProcessStatus
from ..enums import PaymentFlow
from ..enums import Language
from ..enums import Currency
from ..enums import TibAuthorizationStatus
from ..enums import TransferType


class AdminTransfer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransferId = None
            self.RefId = None
            self.RelatedMerchantId = None
            self.RelatedCustomerId = None
            self.PaymentMethodId = None
            self.CurrentStatus = None
            self.PaymentFlowType = None
            self.ForcedCustomerPaymentMethodId = None
            self.IsAutomaticPayment = None
            self.TransferDueDate = None
            self.TransferAmount = None
            self.OverrideLanguage = None
            self.IsMarkResolved = None
            self.ConvenientFeesForCreditCard = None
            self.ConvenientFeesForDirectAccount = None
            self.IsOperationCreated = None
            self.GroupId = None
            self.ExternalReferenceNumber = None
            self.TransferTypeRef = None
            self.IsDeleted = None
            self.CreatedDate = None
            self.OverrideCurrency = None
            self.LimitationStatus = None
            self.ClientAuthorizationStatus = None
            self.ClientAuthorizedBy = None
            self.TIBAuthorizationStatus = None
            self.TIBAuthorizedBy = None
            self.TIBAuthorizationDate = None
            self.ClientAuthorizationDate = None
            self.TransferType = None
            self.AuthorizedPaymentMethodType = None
            self.RecuringTransferId = None
            self.StatementDescription = None
            self.IsArchived = None
            self.AskForCustomerConsent = None
            self.Title = None
            self.Decription = None
            self.ExternalSystemNumber = None
            self.IsChecked = None
            self.TIBAuthorizationStatusValue = None
            self.TransferTypeValue = None
            self.CurrentStatusValue = None
            self.PaymentFlowTypeValue = None
            self.OverrideLanguageValue = None
            self.OverrideCurrencyValue = None

        else:
            
            self.TransferId = getattr(obj, 'TransferId', None)
            self.RefId = getattr(obj, 'RefId', None)
            self.RelatedMerchantId = getattr(obj, 'RelatedMerchantId', None)
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.PaymentMethodId = getattr(obj, 'PaymentMethodId', None)
            self.CurrentStatus = ProcessStatus(getattr(obj, 'CurrentStatus', None)) if getattr(obj, 'CurrentStatus', None) is not None else None
            self.PaymentFlowType = PaymentFlow(getattr(obj, 'PaymentFlowType', None)) if getattr(obj, 'PaymentFlowType', None) is not None else None
            self.ForcedCustomerPaymentMethodId = getattr(obj, 'ForcedCustomerPaymentMethodId', None)
            self.IsAutomaticPayment = getattr(obj, 'IsAutomaticPayment', None)
            self.TransferDueDate = getattr(obj, 'TransferDueDate', None)
            self.TransferAmount = getattr(obj, 'TransferAmount', None)
            self.OverrideLanguage = Language(getattr(obj, 'OverrideLanguage', None)) if getattr(obj, 'OverrideLanguage', None) is not None else None
            self.IsMarkResolved = getattr(obj, 'IsMarkResolved', None)
            self.ConvenientFeesForCreditCard = getattr(obj, 'ConvenientFeesForCreditCard', None)
            self.ConvenientFeesForDirectAccount = getattr(obj, 'ConvenientFeesForDirectAccount', None)
            self.IsOperationCreated = getattr(obj, 'IsOperationCreated', None)
            self.GroupId = getattr(obj, 'GroupId', None)
            self.ExternalReferenceNumber = getattr(obj, 'ExternalReferenceNumber', None)
            self.TransferTypeRef = getattr(obj, 'TransferTypeRef', None)
            self.IsDeleted = getattr(obj, 'IsDeleted', None)
            self.CreatedDate = getattr(obj, 'CreatedDate', None)
            self.OverrideCurrency = Currency(getattr(obj, 'OverrideCurrency', None)) if getattr(obj, 'OverrideCurrency', None) is not None else None
            self.LimitationStatus = getattr(obj, 'LimitationStatus', None)
            self.ClientAuthorizationStatus = getattr(obj, 'ClientAuthorizationStatus', None)
            self.ClientAuthorizedBy = getattr(obj, 'ClientAuthorizedBy', None)
            self.TIBAuthorizationStatus = TibAuthorizationStatus(getattr(obj, 'TIBAuthorizationStatus', None)) if getattr(obj, 'TIBAuthorizationStatus', None) is not None else None
            self.TIBAuthorizedBy = getattr(obj, 'TIBAuthorizedBy', None)
            self.TIBAuthorizationDate = getattr(obj, 'TIBAuthorizationDate', None)
            self.ClientAuthorizationDate = getattr(obj, 'ClientAuthorizationDate', None)
            self.TransferType = TransferType(getattr(obj, 'TransferType', None)) if getattr(obj, 'TransferType', None) is not None else None
            self.AuthorizedPaymentMethodType = getattr(obj, 'AuthorizedPaymentMethodType', None)
            self.RecuringTransferId = getattr(obj, 'RecuringTransferId', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)
            self.IsArchived = getattr(obj, 'IsArchived', None)
            self.AskForCustomerConsent = getattr(obj, 'AskForCustomerConsent', None)
            self.Title = getattr(obj, 'Title', None)
            self.Decription = getattr(obj, 'Decription', None)
            self.ExternalSystemNumber = getattr(obj, 'ExternalSystemNumber', None)
            self.IsChecked = getattr(obj, 'IsChecked', None)
            self.TIBAuthorizationStatusValue = getattr(obj, 'TIBAuthorizationStatusValue', None)
            self.TransferTypeValue = getattr(obj, 'TransferTypeValue', None)
            self.CurrentStatusValue = getattr(obj, 'CurrentStatusValue', None)
            self.PaymentFlowTypeValue = getattr(obj, 'PaymentFlowTypeValue', None)
            self.OverrideLanguageValue = getattr(obj, 'OverrideLanguageValue', None)
            self.OverrideCurrencyValue = getattr(obj, 'OverrideCurrencyValue', None)


