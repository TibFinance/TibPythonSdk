




class DasMonthlyPeriod:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Month = None
            self.Year = None

        else:
            
            self.Month = getattr(obj, 'Month', None)
            self.Year = getattr(obj, 'Year', None)


