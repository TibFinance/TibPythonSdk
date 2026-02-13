




class CheckResultDetail:
    def __init__(self, obj=None):
        if obj is None:
            
            self.EventDate = None
            self.TransacitonAmount = None

        else:
            
            self.EventDate = getattr(obj, 'EventDate', None)
            self.TransacitonAmount = getattr(obj, 'TransacitonAmount', None)


