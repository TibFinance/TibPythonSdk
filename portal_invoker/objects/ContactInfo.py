




class ContactInfo:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Email = None
            self.Phone = None
            self.Address = None
            self.City = None
            self.Province = None
            self.Country = None
            self.ZipCode = None
            self.Language = None

        else:
            
            self.Email = getattr(obj, 'Email', None)
            self.Phone = getattr(obj, 'Phone', None)
            self.Address = getattr(obj, 'Address', None)
            self.City = getattr(obj, 'City', None)
            self.Province = getattr(obj, 'Province', None)
            self.Country = getattr(obj, 'Country', None)
            self.ZipCode = getattr(obj, 'ZipCode', None)
            self.Language = getattr(obj, 'Language', None)


