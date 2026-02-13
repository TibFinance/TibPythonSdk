




class QuestionAnswerDecrypted:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Question = None
            self.Answer = None

        else:
            
            self.Question = getattr(obj, 'Question', None)
            self.Answer = getattr(obj, 'Answer', None)


