




class Payment:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Operations = None

        else:
            
            from .PaymentOperationEntity import PaymentOperationEntity

            self.Operations = []
            if hasattr(obj, 'Operations') and obj.Operations is not None:
                self.Operations = [PaymentOperationEntity(name) for name in  obj.Operations]


