


from ..enums import AcpTransactionType


class ValidationsLimitsRules:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Limit = None
            self.LimitDaily = None
            self.LimitPerBankAccountDaily = None
            self.LimitPerBankAccountPerDelays = None
            self.Delays = None
            self.ClientWarningLimit = None
            self.TIBWarningLimit = None
            self.NumberPerBankAccountDaily = None
            self.NumberPerBankPerDelays = None
            self.TIBWarningLimitPerBankAccountDaily = None
            self.TIBWarningLimitPerBankAccountPerDelays = None
            self.TIBWarningNumberPerBankAccountDaily = None
            self.TIBWarningNumberPerBankPerDelays = None
            self.TIBWarningLimitDaily = None
            self.OperationType = None
            self.ClientLimitDaily = None
            self.TIBWarningClientLimitDaily = None

        else:
            
            self.Limit = getattr(obj, 'Limit', None)
            self.LimitDaily = getattr(obj, 'LimitDaily', None)
            self.LimitPerBankAccountDaily = getattr(obj, 'LimitPerBankAccountDaily', None)
            self.LimitPerBankAccountPerDelays = getattr(obj, 'LimitPerBankAccountPerDelays', None)
            self.Delays = getattr(obj, 'Delays', None)
            self.ClientWarningLimit = getattr(obj, 'ClientWarningLimit', None)
            self.TIBWarningLimit = getattr(obj, 'TIBWarningLimit', None)
            self.NumberPerBankAccountDaily = getattr(obj, 'NumberPerBankAccountDaily', None)
            self.NumberPerBankPerDelays = getattr(obj, 'NumberPerBankPerDelays', None)
            self.TIBWarningLimitPerBankAccountDaily = getattr(obj, 'TIBWarningLimitPerBankAccountDaily', None)
            self.TIBWarningLimitPerBankAccountPerDelays = getattr(obj, 'TIBWarningLimitPerBankAccountPerDelays', None)
            self.TIBWarningNumberPerBankAccountDaily = getattr(obj, 'TIBWarningNumberPerBankAccountDaily', None)
            self.TIBWarningNumberPerBankPerDelays = getattr(obj, 'TIBWarningNumberPerBankPerDelays', None)
            self.TIBWarningLimitDaily = getattr(obj, 'TIBWarningLimitDaily', None)
            self.OperationType = AcpTransactionType(getattr(obj, 'OperationType', None)) if getattr(obj, 'OperationType', None) is not None else None
            self.ClientLimitDaily = getattr(obj, 'ClientLimitDaily', None)
            self.TIBWarningClientLimitDaily = getattr(obj, 'TIBWarningClientLimitDaily', None)


