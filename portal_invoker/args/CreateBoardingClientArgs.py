




class CreateBoardingClientArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Name = None
            self.Email = None
            self.PhoneNumber = None
            self.Language = None
            self.Currency = None

        else:
            
            self.Name = getattr(obj, 'Name', None)
            self.Email = getattr(obj, 'Email', None)
            self.PhoneNumber = getattr(obj, 'PhoneNumber', None)
            self.Language = getattr(obj, 'Language', None)
            self.Currency = getattr(obj, 'Currency', None)


