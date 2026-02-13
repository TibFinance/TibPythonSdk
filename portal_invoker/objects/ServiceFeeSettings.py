


from ..enums import FeeMode
from ..enums import FeeMode
from ..enums import FeeMode
from ..enums import ConvenientFeeMode
from ..enums import ConvenientFeeMode


class ServiceFeeSettings:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CreditCardFeeMode = None
            self.CreditCardPercentageFee = None
            self.CreditCardAbsoluteFee = None
            self.DebitFeeMode = None
            self.DebitPercentageFee = None
            self.DebitAbsoluteFee = None
            self.InstantTransferFeeMode = None
            self.InstantTransferPercentageFee = None
            self.InstantTransferAbsoluteFee = None
            self.ConvenientFeeCreditMode = None
            self.ConvenientFeeCreditPercentageFee = None
            self.ConvenientFeeCreditAbsoluteFee = None
            self.ConvenientFeeCreditRoundUpValue = None
            self.ConvenientFeeDebitMode = None
            self.ConvenientFeeDebitPercentageFee = None
            self.ConvenientFeeDebitAbsoluteFee = None
            self.ConvenientFeeDebitRoundUpValue = None
            self.DebitFeeRoundUpValue = None
            self.CreditCardFeeRoundUpValue = None
            self.InstantTransferFeeRoundUpValue = None
            self.RevertCreditCardAbsoluteFees = None
            self.RevertCreditCardPercentageFees = None
            self.RevertDebitAbsoluteFees = None
            self.RevertDebitPercentageFees = None
            self.InteracFeeAbsolute = None
            self.InteracFeePercentage = None
            self.InteracFeeCollectAbsolute = None
            self.InteracFeeCollectPercentage = None
            self.DebitNFSFees = None
            self.NFSFileFees = None
            self.DataContext = None

        else:
            
            self.CreditCardFeeMode = FeeMode(getattr(obj, 'CreditCardFeeMode', None)) if getattr(obj, 'CreditCardFeeMode', None) is not None else None
            self.CreditCardPercentageFee = getattr(obj, 'CreditCardPercentageFee', None)
            self.CreditCardAbsoluteFee = getattr(obj, 'CreditCardAbsoluteFee', None)
            self.DebitFeeMode = FeeMode(getattr(obj, 'DebitFeeMode', None)) if getattr(obj, 'DebitFeeMode', None) is not None else None
            self.DebitPercentageFee = getattr(obj, 'DebitPercentageFee', None)
            self.DebitAbsoluteFee = getattr(obj, 'DebitAbsoluteFee', None)
            self.InstantTransferFeeMode = FeeMode(getattr(obj, 'InstantTransferFeeMode', None)) if getattr(obj, 'InstantTransferFeeMode', None) is not None else None
            self.InstantTransferPercentageFee = getattr(obj, 'InstantTransferPercentageFee', None)
            self.InstantTransferAbsoluteFee = getattr(obj, 'InstantTransferAbsoluteFee', None)
            self.ConvenientFeeCreditMode = ConvenientFeeMode(getattr(obj, 'ConvenientFeeCreditMode', None)) if getattr(obj, 'ConvenientFeeCreditMode', None) is not None else None
            self.ConvenientFeeCreditPercentageFee = getattr(obj, 'ConvenientFeeCreditPercentageFee', None)
            self.ConvenientFeeCreditAbsoluteFee = getattr(obj, 'ConvenientFeeCreditAbsoluteFee', None)
            self.ConvenientFeeCreditRoundUpValue = getattr(obj, 'ConvenientFeeCreditRoundUpValue', None)
            self.ConvenientFeeDebitMode = ConvenientFeeMode(getattr(obj, 'ConvenientFeeDebitMode', None)) if getattr(obj, 'ConvenientFeeDebitMode', None) is not None else None
            self.ConvenientFeeDebitPercentageFee = getattr(obj, 'ConvenientFeeDebitPercentageFee', None)
            self.ConvenientFeeDebitAbsoluteFee = getattr(obj, 'ConvenientFeeDebitAbsoluteFee', None)
            self.ConvenientFeeDebitRoundUpValue = getattr(obj, 'ConvenientFeeDebitRoundUpValue', None)
            self.DebitFeeRoundUpValue = getattr(obj, 'DebitFeeRoundUpValue', None)
            self.CreditCardFeeRoundUpValue = getattr(obj, 'CreditCardFeeRoundUpValue', None)
            self.InstantTransferFeeRoundUpValue = getattr(obj, 'InstantTransferFeeRoundUpValue', None)
            self.RevertCreditCardAbsoluteFees = getattr(obj, 'RevertCreditCardAbsoluteFees', None)
            self.RevertCreditCardPercentageFees = getattr(obj, 'RevertCreditCardPercentageFees', None)
            self.RevertDebitAbsoluteFees = getattr(obj, 'RevertDebitAbsoluteFees', None)
            self.RevertDebitPercentageFees = getattr(obj, 'RevertDebitPercentageFees', None)
            self.InteracFeeAbsolute = getattr(obj, 'InteracFeeAbsolute', None)
            self.InteracFeePercentage = getattr(obj, 'InteracFeePercentage', None)
            self.InteracFeeCollectAbsolute = getattr(obj, 'InteracFeeCollectAbsolute', None)
            self.InteracFeeCollectPercentage = getattr(obj, 'InteracFeeCollectPercentage', None)
            self.DebitNFSFees = getattr(obj, 'DebitNFSFees', None)
            self.NFSFileFees = getattr(obj, 'NFSFileFees', None)
            self.DataContext = getattr(obj, 'DataContext', None)


