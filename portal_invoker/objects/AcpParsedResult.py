


from ..enums import AcpTransactionType


class AcpParsedResult:
    def __init__(self, obj=None):
        if obj is None:
            
            self.FirstLine = None
            self.AllTransactions = None
            self.LastLine = None

        else:
            
            from .LineBaseWithHeader import LineBaseWithHeader
            from .BaseLastLine import BaseLastLine
            self.FirstLine = LineBaseWithHeader(getattr(obj, 'FirstLine', None)) if getattr(obj, 'FirstLine', None) is not None else None

            self.AllTransactions = []
            if hasattr(obj, 'AllTransactions') and obj.AllTransactions is not None:
                self.AllTransactions = [AcpTransactionType(name) for name in  obj.AllTransactions]
            self.LastLine = BaseLastLine(getattr(obj, 'LastLine', None)) if getattr(obj, 'LastLine', None) is not None else None


