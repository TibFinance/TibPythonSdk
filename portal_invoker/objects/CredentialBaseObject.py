




class CredentialBaseObject:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Username = None
            self.Username2 = None
            self.Password = None
            self.Password2 = None
            self.Questions = None
            self.Addresses = None

        else:
            
            from .QuestionAnswer import QuestionAnswer
            from .ProviderAddressEntity import ProviderAddressEntity
            self.Username = getattr(obj, 'Username', None)
            self.Username2 = getattr(obj, 'Username2', None)
            self.Password = getattr(obj, 'Password', None)
            self.Password2 = getattr(obj, 'Password2', None)

            self.Questions = []
            if hasattr(obj, 'Questions') and obj.Questions is not None:
                self.Questions = [QuestionAnswer(name) for name in  obj.Questions]

            self.Addresses = []
            if hasattr(obj, 'Addresses') and obj.Addresses is not None:
                self.Addresses = [ProviderAddressEntity(name) for name in  obj.Addresses]


