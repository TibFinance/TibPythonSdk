




class CreateAdminSessionArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.TemporaryAdminCode = None

        else:
            
            self.TemporaryAdminCode = getattr(obj, 'TemporaryAdminCode', None)


