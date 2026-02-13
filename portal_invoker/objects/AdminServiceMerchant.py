




class AdminServiceMerchant:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ServiceId = None
            self.MerchantId = None
            self.MerchantAccountId = None
            self.ServiceName = None
            self.MerchantName = None
            self.MerchantEmail = None
            self.PhoneNumber = None
            self.MerchantDescription = None
            self.AccountName = None
            self.AccountInformationView = None
            self.IsActive = None
            self.IsDeletedService = None
            self.IsDeletedMerchant = None
            self.IsAuthorizedMerchant = None
            self.IsClientMerchant = None
            self.WhiteLabelingId = None
            self.DefaultStatementDescription = None
            self.CreatedDateService = None
            self.CreatedDateMerchant = None
            self.IsDeletedMerchantAccount = None
            self.IsActiveService = None
            self.IsChecked = None

        else:
            
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.MerchantAccountId = getattr(obj, 'MerchantAccountId', None)
            self.ServiceName = getattr(obj, 'ServiceName', None)
            self.MerchantName = getattr(obj, 'MerchantName', None)
            self.MerchantEmail = getattr(obj, 'MerchantEmail', None)
            self.PhoneNumber = getattr(obj, 'PhoneNumber', None)
            self.MerchantDescription = getattr(obj, 'MerchantDescription', None)
            self.AccountName = getattr(obj, 'AccountName', None)
            self.AccountInformationView = getattr(obj, 'AccountInformationView', None)
            self.IsActive = getattr(obj, 'IsActive', None)
            self.IsDeletedService = getattr(obj, 'IsDeletedService', None)
            self.IsDeletedMerchant = getattr(obj, 'IsDeletedMerchant', None)
            self.IsAuthorizedMerchant = getattr(obj, 'IsAuthorizedMerchant', None)
            self.IsClientMerchant = getattr(obj, 'IsClientMerchant', None)
            self.WhiteLabelingId = getattr(obj, 'WhiteLabelingId', None)
            self.DefaultStatementDescription = getattr(obj, 'DefaultStatementDescription', None)
            self.CreatedDateService = getattr(obj, 'CreatedDateService', None)
            self.CreatedDateMerchant = getattr(obj, 'CreatedDateMerchant', None)
            self.IsDeletedMerchantAccount = getattr(obj, 'IsDeletedMerchantAccount', None)
            self.IsActiveService = getattr(obj, 'IsActiveService', None)
            self.IsChecked = getattr(obj, 'IsChecked', None)


