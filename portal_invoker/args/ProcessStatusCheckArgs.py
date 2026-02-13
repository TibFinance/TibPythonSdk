


from ..objects import TransactionIdentity
from ..objects import TransactionMailingInfo
from ..objects import ProviderAccount


class ProcessStatusCheckArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Transactions = None
            self.MailingInfo = None
            self.ProviderCredentials = None
            self.TransactionsCompressed = None

        else:
            

            self.Transactions = []
            if hasattr(obj, 'Transactions') and obj.Transactions is not None:
                self.Transactions = [TransactionIdentity(name) for name in  obj.Transactions]
            self.MailingInfo = TransactionMailingInfo(getattr(obj, 'MailingInfo', None)) if getattr(obj, 'MailingInfo', None) is not None else None

            self.ProviderCredentials = []
            if hasattr(obj, 'ProviderCredentials') and obj.ProviderCredentials is not None:
                self.ProviderCredentials = [ProviderAccount(name) for name in  obj.ProviderCredentials]
            self.TransactionsCompressed = getattr(obj, 'TransactionsCompressed', None)


