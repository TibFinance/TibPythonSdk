




class MonerisCredenitals:
    def __init__(self, obj=None):
        if obj is None:
            
            self.StoreID = None
            self.ApiToken = None
            self.CountryCode = None
            self.Crypt = None
            self.CvdIdicator = None

        else:
            
            self.StoreID = getattr(obj, 'StoreID', None)
            self.ApiToken = getattr(obj, 'ApiToken', None)
            self.CountryCode = getattr(obj, 'CountryCode', None)
            self.Crypt = getattr(obj, 'Crypt', None)
            self.CvdIdicator = getattr(obj, 'CvdIdicator', None)


