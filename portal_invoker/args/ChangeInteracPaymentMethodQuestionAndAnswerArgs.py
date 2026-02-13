




class ChangeInteracPaymentMethodQuestionAndAnswerArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.InteracPaymentMethodId = None
            self.InteracQuestion = None
            self.InteracAnswer = None
            self.MerchantId = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.InteracPaymentMethodId = getattr(obj, 'InteracPaymentMethodId', None)
            self.InteracQuestion = getattr(obj, 'InteracQuestion', None)
            self.InteracAnswer = getattr(obj, 'InteracAnswer', None)
            self.MerchantId = getattr(obj, 'MerchantId', None)


