




class MarkPaymentResolvedArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ListOfPayment = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)

            self.ListOfPayment = []
            if hasattr(obj, 'ListOfPayment') and obj.ListOfPayment is not None:
                self.ListOfPayment = [name for name in obj.ListOfPayment]


