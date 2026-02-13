




class PaymentMethodAddRequest:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MerchantInfo = None
            self.TransferInfo = None
            self.CustomerInfo = None
            self.CustomerExistingPaymentMethods = None
            self.RelatedBillInfo = None

        else:
            
            from .MerchantView import MerchantView
            from .PaymentEntity import PaymentEntity
            from .Customer import Customer
            from .PaymentMethod import PaymentMethod
            from .Bill import Bill
            self.MerchantInfo = MerchantView(getattr(obj, 'MerchantInfo', None)) if getattr(obj, 'MerchantInfo', None) is not None else None
            self.TransferInfo = PaymentEntity(getattr(obj, 'TransferInfo', None)) if getattr(obj, 'TransferInfo', None) is not None else None
            self.CustomerInfo = Customer(getattr(obj, 'CustomerInfo', None)) if getattr(obj, 'CustomerInfo', None) is not None else None

            self.CustomerExistingPaymentMethods = []
            if hasattr(obj, 'CustomerExistingPaymentMethods') and obj.CustomerExistingPaymentMethods is not None:
                self.CustomerExistingPaymentMethods = [PaymentMethod(name) for name in  obj.CustomerExistingPaymentMethods]
            self.RelatedBillInfo = Bill(getattr(obj, 'RelatedBillInfo', None)) if getattr(obj, 'RelatedBillInfo', None) is not None else None


