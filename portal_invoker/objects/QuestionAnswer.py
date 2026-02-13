




class QuestionAnswer:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Question = None
            self.CryptedAnswer = None

        else:
            
            self.Question = getattr(obj, 'Question', None)
            self.CryptedAnswer = getattr(obj, 'CryptedAnswer', None)


