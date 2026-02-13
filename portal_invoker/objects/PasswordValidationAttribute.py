




class PasswordValidationAttribute:
    def __init__(self, obj=None):
        if obj is None:
            
            self.MinLength = None
            self.MaxLength = None
            self.RequireUppercase = None
            self.RequireLowercase = None
            self.RequireDigit = None
            self.RequireSpecialChar = None
            self.SpecialCharacters = None

        else:
            
            self.MinLength = getattr(obj, 'MinLength', None)
            self.MaxLength = getattr(obj, 'MaxLength', None)
            self.RequireUppercase = getattr(obj, 'RequireUppercase', None)
            self.RequireLowercase = getattr(obj, 'RequireLowercase', None)
            self.RequireDigit = getattr(obj, 'RequireDigit', None)
            self.RequireSpecialChar = getattr(obj, 'RequireSpecialChar', None)
            self.SpecialCharacters = getattr(obj, 'SpecialCharacters', None)


