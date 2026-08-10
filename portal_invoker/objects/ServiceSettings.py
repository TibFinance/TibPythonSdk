




class ServiceSettings:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CollectionLimit = None
            self.CollectionLimitDaily = None
            self.DepositLimit = None
            self.DepositLimitDaily = None
            self.DelayBufferAmount = None
            self.RemainingAmount = None
            self.WalletBalance = None
            self.IsWalletFeatureActive = None
            self.WalletType = None
            self.NsfBuffer = None
            self.CollectionLimitPerBankAccountDaily = None
            self.CollectionLimitPerBankAccountPerDelays = None
            self.CollectionLimitPerBankAccountHoursDelays = None
            self.ClientWarningCollectionLimit = None
            self.NumberOfCollectionPerBankAccountDaily = None
            self.NumberOfCollectionPerBankPerDelays = None
            self.DepositLimitPerBankAccountDaily = None
            self.DepositLimitPerBankAccountPerDelays = None
            self.DepositLimitPerBankAccountHoursDelays = None
            self.ClientWarningDepositLimit = None
            self.NumberOfDepositPerBankAccountDaily = None
            self.NumberOfDepositPerBankPerDelays = None
            self.MerchantAccountDepositDelay = None
            self.CollectAllowedPaymentMethods = None
            self.DepositAllowedPaymentMethods = None
            self.DenyFreeDeposits = None
            self.DenySupplierPayments = None

        else:
            
            self.CollectionLimit = getattr(obj, 'CollectionLimit', None)
            self.CollectionLimitDaily = getattr(obj, 'CollectionLimitDaily', None)
            self.DepositLimit = getattr(obj, 'DepositLimit', None)
            self.DepositLimitDaily = getattr(obj, 'DepositLimitDaily', None)
            self.DelayBufferAmount = getattr(obj, 'DelayBufferAmount', None)
            self.RemainingAmount = getattr(obj, 'RemainingAmount', None)
            self.WalletBalance = getattr(obj, 'WalletBalance', None)
            self.IsWalletFeatureActive = getattr(obj, 'IsWalletFeatureActive', None)
            self.WalletType = getattr(obj, 'WalletType', None)
            self.NsfBuffer = getattr(obj, 'NsfBuffer', None)
            self.CollectionLimitPerBankAccountDaily = getattr(obj, 'CollectionLimitPerBankAccountDaily', None)
            self.CollectionLimitPerBankAccountPerDelays = getattr(obj, 'CollectionLimitPerBankAccountPerDelays', None)
            self.CollectionLimitPerBankAccountHoursDelays = getattr(obj, 'CollectionLimitPerBankAccountHoursDelays', None)
            self.ClientWarningCollectionLimit = getattr(obj, 'ClientWarningCollectionLimit', None)
            self.NumberOfCollectionPerBankAccountDaily = getattr(obj, 'NumberOfCollectionPerBankAccountDaily', None)
            self.NumberOfCollectionPerBankPerDelays = getattr(obj, 'NumberOfCollectionPerBankPerDelays', None)
            self.DepositLimitPerBankAccountDaily = getattr(obj, 'DepositLimitPerBankAccountDaily', None)
            self.DepositLimitPerBankAccountPerDelays = getattr(obj, 'DepositLimitPerBankAccountPerDelays', None)
            self.DepositLimitPerBankAccountHoursDelays = getattr(obj, 'DepositLimitPerBankAccountHoursDelays', None)
            self.ClientWarningDepositLimit = getattr(obj, 'ClientWarningDepositLimit', None)
            self.NumberOfDepositPerBankAccountDaily = getattr(obj, 'NumberOfDepositPerBankAccountDaily', None)
            self.NumberOfDepositPerBankPerDelays = getattr(obj, 'NumberOfDepositPerBankPerDelays', None)
            self.MerchantAccountDepositDelay = getattr(obj, 'MerchantAccountDepositDelay', None)
            self.CollectAllowedPaymentMethods = getattr(obj, 'CollectAllowedPaymentMethods', None)
            self.DepositAllowedPaymentMethods = getattr(obj, 'DepositAllowedPaymentMethods', None)
            self.DenyFreeDeposits = getattr(obj, 'DenyFreeDeposits', None)
            self.DenySupplierPayments = getattr(obj, 'DenySupplierPayments', None)


