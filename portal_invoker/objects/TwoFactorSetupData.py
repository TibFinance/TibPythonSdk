




class TwoFactorSetupData:
    def __init__(self, obj=None):
        if obj is None:
            
            self.QrCodeBase64 = None
            self.ManualEntryKey = None
            self.OtpAuthUri = None
            self.Issuer = None
            self.AccountName = None

        else:
            
            self.QrCodeBase64 = getattr(obj, 'QrCodeBase64', None)
            self.ManualEntryKey = getattr(obj, 'ManualEntryKey', None)
            self.OtpAuthUri = getattr(obj, 'OtpAuthUri', None)
            self.Issuer = getattr(obj, 'Issuer', None)
            self.AccountName = getattr(obj, 'AccountName', None)


