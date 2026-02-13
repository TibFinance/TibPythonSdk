


from ..objects import ConvenientFeeSettings


class AddOrUpdateConvenientFeeSettingsForMerchantArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ConvenientFeeSettings = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ConvenientFeeSettings = ConvenientFeeSettings(getattr(obj, 'ConvenientFeeSettings', None)) if getattr(obj, 'ConvenientFeeSettings', None) is not None else None


