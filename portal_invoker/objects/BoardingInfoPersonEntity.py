




class BoardingInfoPersonEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BoardingInfoPersonId = None
            self.FirstName = None
            self.LastName = None
            self.Address = None
            self.Country = None
            self.State = None
            self.City = None
            self.Zip = None
            self.Phone = None
            self.BirthDate = None
            self.GovId = None
            self.SharePercentage = None
            self.IsRepresentant = None

        else:
            
            self.BoardingInfoPersonId = getattr(obj, 'BoardingInfoPersonId', None)
            self.FirstName = getattr(obj, 'FirstName', None)
            self.LastName = getattr(obj, 'LastName', None)
            self.Address = getattr(obj, 'Address', None)
            self.Country = getattr(obj, 'Country', None)
            self.State = getattr(obj, 'State', None)
            self.City = getattr(obj, 'City', None)
            self.Zip = getattr(obj, 'Zip', None)
            self.Phone = getattr(obj, 'Phone', None)
            self.BirthDate = getattr(obj, 'BirthDate', None)
            self.GovId = getattr(obj, 'GovId', None)
            self.SharePercentage = getattr(obj, 'SharePercentage', None)
            self.IsRepresentant = getattr(obj, 'IsRepresentant', None)


