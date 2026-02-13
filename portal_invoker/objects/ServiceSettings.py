




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
            self.TIBWarningCollectionLimit = None
            self.TIBWarningCollectionLimitPerBankAccountDaily = None
            self.TIBWarningCollectionLimitPerBankAccountPerDelays = None
            self.TIBWarningNumberOfCollectionPerBankAccountDaily = None
            self.TIBWarningNumberOfCollectionPerBankPerDelays = None
            self.TIBWarningCollectionLimitDaily = None
            self.TIBWarningDepositLimit = None
            self.TIBWarningDepositLimitPerBankAccountDaily = None
            self.TIBWarningDepositLimitPerBankAccountPerDelays = None
            self.TIBWarningNumberOfDepositPerBankAccountDaily = None
            self.TIBWarningNumberOfDepositPerBankPerDelays = None
            self.TIBWarningDepositLimitDaily = None
            self.MerchantAccountDepositDelay = None
            self.DataContext = None

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
            self.TIBWarningCollectionLimit = getattr(obj, 'TIBWarningCollectionLimit', None)
            self.TIBWarningCollectionLimitPerBankAccountDaily = getattr(obj, 'TIBWarningCollectionLimitPerBankAccountDaily', None)
            self.TIBWarningCollectionLimitPerBankAccountPerDelays = getattr(obj, 'TIBWarningCollectionLimitPerBankAccountPerDelays', None)
            self.TIBWarningNumberOfCollectionPerBankAccountDaily = getattr(obj, 'TIBWarningNumberOfCollectionPerBankAccountDaily', None)
            self.TIBWarningNumberOfCollectionPerBankPerDelays = getattr(obj, 'TIBWarningNumberOfCollectionPerBankPerDelays', None)
            self.TIBWarningCollectionLimitDaily = getattr(obj, 'TIBWarningCollectionLimitDaily', None)
            self.TIBWarningDepositLimit = getattr(obj, 'TIBWarningDepositLimit', None)
            self.TIBWarningDepositLimitPerBankAccountDaily = getattr(obj, 'TIBWarningDepositLimitPerBankAccountDaily', None)
            self.TIBWarningDepositLimitPerBankAccountPerDelays = getattr(obj, 'TIBWarningDepositLimitPerBankAccountPerDelays', None)
            self.TIBWarningNumberOfDepositPerBankAccountDaily = getattr(obj, 'TIBWarningNumberOfDepositPerBankAccountDaily', None)
            self.TIBWarningNumberOfDepositPerBankPerDelays = getattr(obj, 'TIBWarningNumberOfDepositPerBankPerDelays', None)
            self.TIBWarningDepositLimitDaily = getattr(obj, 'TIBWarningDepositLimitDaily', None)
            self.MerchantAccountDepositDelay = getattr(obj, 'MerchantAccountDepositDelay', None)
            self.DataContext = getattr(obj, 'DataContext', None)


