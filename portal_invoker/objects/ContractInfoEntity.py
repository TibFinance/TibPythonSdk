




class ContractInfoEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BoardingCompanyInfos = None
            self.FeeSettings = None
            self.LimitationSettings = None
            self.IsSignedContract = None
            self.ClientId = None
            self.MerchantId = None

        else:
            
            from .BoardingInformationEntity import BoardingInformationEntity
            from .ServiceFeeSettings import ServiceFeeSettings
            from .ServiceSettings import ServiceSettings
            self.BoardingCompanyInfos = BoardingInformationEntity(getattr(obj, 'BoardingCompanyInfos', None)) if getattr(obj, 'BoardingCompanyInfos', None) is not None else None
            self.FeeSettings = ServiceFeeSettings(getattr(obj, 'FeeSettings', None)) if getattr(obj, 'FeeSettings', None) is not None else None
            self.LimitationSettings = ServiceSettings(getattr(obj, 'LimitationSettings', None)) if getattr(obj, 'LimitationSettings', None) is not None else None
            self.IsSignedContract = getattr(obj, 'IsSignedContract', None)
            self.ClientId = getattr(obj, 'ClientId', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


