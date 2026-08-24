




class Verify2FASetupArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.TwoFactorCode = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.TwoFactorCode = getattr(obj, 'TwoFactorCode', None)


