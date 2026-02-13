




class ErrorReportDataArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.Dateformat = None
            self.Interval = None
            self.MerchantId = None
            self.ServiceId = None
            self.FromDate = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.Dateformat = getattr(obj, 'Dateformat', None)
            self.Interval = getattr(obj, 'Interval', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.FromDate = getattr(obj, 'FromDate', None)


