




class BlueSnapWebhookArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TransactionType = None
            self.WebhookDatas = None

        else:
            
            self.TransactionType = getattr(obj, 'TransactionType', None)

            self.WebhookDatas = []
            if hasattr(obj, 'WebhookDatas') and obj.WebhookDatas is not None:
                self.WebhookDatas = [name for name in obj.WebhookDatas]


