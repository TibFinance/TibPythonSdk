
from ..utility import to_enum

from ..enums import TransferType
from ..enums import PaymentMethodType


class TransferBatchItem:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ReferenceNumber = None
            self.TransferType = None
            self.PaymentMethodType = None
            self.Amount = None
            self.TransactionDueDate = None
            self.StatementDescription = None
            self.ImmediateTransfer = None
            self.Customer = None
            self.BankAccount = None
            self.InteracInformation = None

        else:
            
            from .TransferBatchCustomer import TransferBatchCustomer
            from .Account import Account
            from .Interac import Interac
            self.ReferenceNumber = getattr(obj, 'ReferenceNumber', None)
            self.TransferType = to_enum(TransferType, getattr(obj, 'TransferType', None))
            self.PaymentMethodType = to_enum(PaymentMethodType, getattr(obj, 'PaymentMethodType', None))
            self.Amount = getattr(obj, 'Amount', None)
            self.TransactionDueDate = getattr(obj, 'TransactionDueDate', None)
            self.StatementDescription = getattr(obj, 'StatementDescription', None)
            self.ImmediateTransfer = getattr(obj, 'ImmediateTransfer', None)
            self.Customer = TransferBatchCustomer(getattr(obj, 'Customer', None)) if getattr(obj, 'Customer', None) is not None else None
            self.BankAccount = Account(getattr(obj, 'BankAccount', None)) if getattr(obj, 'BankAccount', None) is not None else None
            self.InteracInformation = Interac(getattr(obj, 'InteracInformation', None)) if getattr(obj, 'InteracInformation', None) is not None else None


