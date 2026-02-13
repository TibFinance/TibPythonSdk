




class BoardingBaseError:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ErrorName = None
            self.Code = None
            self.Description = None

        else:
            
            self.ErrorName = getattr(obj, 'ErrorName', None)
            self.Code = getattr(obj, 'Code', None)
            self.Description = getattr(obj, 'Description', None)


