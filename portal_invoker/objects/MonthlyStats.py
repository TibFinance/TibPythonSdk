




class MonthlyStats:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransactionCategory = None
            self.YearMonth = None
            self.NumberOfTransactions = None
            self.AmountOfTransactions = None

        else:
            
            self.TransactionCategory = getattr(obj, 'TransactionCategory', None)
            self.YearMonth = getattr(obj, 'YearMonth', None)
            self.NumberOfTransactions = getattr(obj, 'NumberOfTransactions', None)
            self.AmountOfTransactions = getattr(obj, 'AmountOfTransactions', None)


