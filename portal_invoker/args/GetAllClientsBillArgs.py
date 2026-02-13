




class GetAllClientsBillArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Year = None
            self.Month = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Year = getattr(obj, 'Year', None)
            self.Month = getattr(obj, 'Month', None)


