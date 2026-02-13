




class TransactionMailingInfo:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MailBody = None
            self.MailSubject = None
            self.ToAddress = None
            self.FromAddress = None

        else:
            
            self.MailBody = getattr(obj, 'MailBody', None)
            self.MailSubject = getattr(obj, 'MailSubject', None)
            self.ToAddress = getattr(obj, 'ToAddress', None)
            self.FromAddress = getattr(obj, 'FromAddress', None)


