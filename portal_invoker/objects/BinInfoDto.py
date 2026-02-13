




class BinInfoDto:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Bin = None
            self.Brand = None
            self.CardType = None
            self.Category = None
            self.CountryCode = None
            self.CountryName = None
            self.PricingGroup = None

        else:
            
            self.Bin = getattr(obj, 'Bin', None)
            self.Brand = getattr(obj, 'Brand', None)
            self.CardType = getattr(obj, 'CardType', None)
            self.Category = getattr(obj, 'Category', None)
            self.CountryCode = getattr(obj, 'CountryCode', None)
            self.CountryName = getattr(obj, 'CountryName', None)
            self.PricingGroup = getattr(obj, 'PricingGroup', None)


