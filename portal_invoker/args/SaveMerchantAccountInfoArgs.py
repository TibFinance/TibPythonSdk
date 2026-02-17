


from ..objects import Account


class SaveMerchantAccountInfoArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.MerchantId = None
            self.Account = None
            self.TwoFactorCode = None
            self.TwoFactorSecurityAnswer = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.Account = Account(getattr(obj, 'Account', None)) if getattr(obj, 'Account', None) is not None else None
            self.TwoFactorCode = getattr(obj, 'TwoFactorCode', None)
            self.TwoFactorSecurityAnswer = getattr(obj, 'TwoFactorSecurityAnswer', None)


