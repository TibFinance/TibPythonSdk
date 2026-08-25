

from .PaymentBaseWithHierarchy import PaymentBaseWithHierarchy


class Payment(PaymentBaseWithHierarchy):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Operations = None

        else:
            super().__init__(obj)
            from .PaymentOperationEntity import PaymentOperationEntity

            self.Operations = []
            if hasattr(obj, 'Operations') and obj.Operations is not None:
                self.Operations = [PaymentOperationEntity(name) for name in  obj.Operations]


