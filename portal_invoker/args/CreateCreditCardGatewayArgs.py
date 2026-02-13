


from ..enums import Currency
from ..objects import CreditCard
from ..enums import Language
from ..enums import PublicAccessTokenRoutingType


class CreateCreditCardGatewayArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.PublicTokenId = None
            self.Currency = None
            self.IsCustomerAutomaticPaymentMethod = None
            self.provider = None
            self.CreditCard = None
            self.IsCustomerPreAutorized = None
            self.IsGatewayCall = None
            self.SkipValidation = None
            self.IsImmediate = None
            self.MerchantId = None
            self.BinCategory = None
            self.CardCategory = None
            self.CardSubType = None
            self.CcBin = None
            self.CcType = None
            self.IsRegulatedCard = None
            self.IssuingCountry = None
            self.Token = None
            self.Exp = None
            self.Last4Digits = None
            self.CardOwner = None
            self.ZipCode = None
            self.Language = None
            self.RoutingType = None

        else:
            
            self.PublicTokenId = getattr(obj, 'PublicTokenId', None)
            self.Currency = Currency(getattr(obj, 'Currency', None)) if getattr(obj, 'Currency', None) is not None else None
            self.IsCustomerAutomaticPaymentMethod = getattr(obj, 'IsCustomerAutomaticPaymentMethod', None)
            self.provider = getattr(obj, 'provider', None)
            self.CreditCard = CreditCard(getattr(obj, 'CreditCard', None)) if getattr(obj, 'CreditCard', None) is not None else None
            self.IsCustomerPreAutorized = getattr(obj, 'IsCustomerPreAutorized', None)
            self.IsGatewayCall = getattr(obj, 'IsGatewayCall', None)
            self.SkipValidation = getattr(obj, 'SkipValidation', None)
            self.IsImmediate = getattr(obj, 'IsImmediate', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.BinCategory = getattr(obj, 'BinCategory', None)
            self.CardCategory = getattr(obj, 'CardCategory', None)
            self.CardSubType = getattr(obj, 'CardSubType', None)
            self.CcBin = getattr(obj, 'CcBin', None)
            self.CcType = getattr(obj, 'CcType', None)
            self.IsRegulatedCard = getattr(obj, 'IsRegulatedCard', None)
            self.IssuingCountry = getattr(obj, 'IssuingCountry', None)
            self.Token = getattr(obj, 'Token', None)
            self.Exp = getattr(obj, 'Exp', None)
            self.Last4Digits = getattr(obj, 'Last4Digits', None)
            self.CardOwner = getattr(obj, 'CardOwner', None)
            self.ZipCode = getattr(obj, 'ZipCode', None)
            self.Language = Language(getattr(obj, 'Language', None)) if getattr(obj, 'Language', None) is not None else None
            self.RoutingType = PublicAccessTokenRoutingType(getattr(obj, 'RoutingType', None)) if getattr(obj, 'RoutingType', None) is not None else None


