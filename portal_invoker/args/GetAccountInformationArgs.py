


from ..objects import ProviderAccount


class GetAccountInformationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ProvidersToCall = None

        else:
            

            self.ProvidersToCall = []
            if hasattr(obj, 'ProvidersToCall') and obj.ProvidersToCall is not None:
                self.ProvidersToCall = [ProviderAccount(name) for name in  obj.ProvidersToCall]


