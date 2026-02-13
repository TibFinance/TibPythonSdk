




class GetConsolidationInternalReportArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.AdminSessionToken = None
            self.Month = None
            self.Year = None
            self.SplitGroupId = None
            self.UseCollection = None

        else:
            
            self.AdminSessionToken = getattr(obj, 'AdminSessionToken', None)
            self.Month = getattr(obj, 'Month', None)
            self.Year = getattr(obj, 'Year', None)
            self.SplitGroupId = getattr(obj, 'SplitGroupId', None)
            self.UseCollection = getattr(obj, 'UseCollection', None)


