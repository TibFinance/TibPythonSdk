


from ..objects import Account


class FinalizeTransferWithExternalSupplierFinancialInformationsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.SupplierAccountAlreadyExists = None
            self.Account = None
            self.CustomerConsent = None
            self.PreAuthorizationGivenForThisMerchant = None
            self.PreAuthorizationGivenForAllMerchants = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.SupplierAccountAlreadyExists = getattr(obj, 'SupplierAccountAlreadyExists', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None
            self.CustomerConsent = getattr(obj, 'CustomerConsent', None)
            self.PreAuthorizationGivenForThisMerchant = getattr(obj, 'PreAuthorizationGivenForThisMerchant', None)
            self.PreAuthorizationGivenForAllMerchants = getattr(obj, 'PreAuthorizationGivenForAllMerchants', None)


