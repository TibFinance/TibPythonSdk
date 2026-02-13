




class Interac:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Description = None
            self.Owner = None
            self.TargetEmailAddress = None
            self.TargetMobilePhoneNumber = None
            self.InteracQuestion = None
            self.InteracAnswer = None

        else:
            
            self.Description = getattr(obj, 'Description', None)
            self.Owner = getattr(obj, 'Owner', None)
            self.TargetEmailAddress = getattr(obj, 'TargetEmailAddress', None)
            self.TargetMobilePhoneNumber = getattr(obj, 'TargetMobilePhoneNumber', None)
            self.InteracQuestion = getattr(obj, 'InteracQuestion', None)
            self.InteracAnswer = getattr(obj, 'InteracAnswer', None)


