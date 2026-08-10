
from ..utility import to_enum

from ..enums import Currency
from ..enums import Language


class BillEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantId = None
            self.BillTitle = None
            self.BillDescription = None
            self.BillAmount = None
            self.ExternalSystemBillNumber1 = None
            self.ExternalSystemBillNumber2 = None
            self.ExternalSystemBillNumber3 = None
            self.BillCurrency = None
            self.Language = None
            self.RelatedCustomerId = None
            self.UseConvenientFeeRule = None

        else:
            
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.BillTitle = getattr(obj, 'BillTitle', None)
            self.BillDescription = getattr(obj, 'BillDescription', None)
            self.BillAmount = getattr(obj, 'BillAmount', None)
            self.ExternalSystemBillNumber1 = getattr(obj, 'ExternalSystemBillNumber1', None)
            self.ExternalSystemBillNumber2 = getattr(obj, 'ExternalSystemBillNumber2', None)
            self.ExternalSystemBillNumber3 = getattr(obj, 'ExternalSystemBillNumber3', None)
            self.BillCurrency = to_enum(Currency, getattr(obj, 'BillCurrency', None))
            self.Language = to_enum(Language, getattr(obj, 'Language', None))
            self.RelatedCustomerId = getattr(obj, 'RelatedCustomerId', None)
            self.UseConvenientFeeRule = getattr(obj, 'UseConvenientFeeRule', None)


