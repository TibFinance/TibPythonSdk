




class SendAllClientBillsArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.MerchantId = None
            self.Year = None
            self.Month = None
            self.SendToQuickbook = None
            self.SendToQuickbookByEmail = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Year = getattr(obj, 'Year', None)
            self.Month = getattr(obj, 'Month', None)
            self.SendToQuickbook = getattr(obj, 'SendToQuickbook', None)
            self.SendToQuickbookByEmail = getattr(obj, 'SendToQuickbookByEmail', None)


