




class DasDateField:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Day = None
            self.Month = None
            self.Year = None
            self.DateTimeValue = None

        else:
            
            self.Day = getattr(obj, 'Day', None)
            self.Month = getattr(obj, 'Month', None)
            self.Year = getattr(obj, 'Year', None)
            self.DateTimeValue = getattr(obj, 'DateTimeValue', None)


