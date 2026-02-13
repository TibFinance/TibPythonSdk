


from ..enums import CredentialType


class CredentialValueType:
    def __init__(self, obj=None):
        if obj is None:
            
            self.CredentialType = None
            self.CredentialValue = None

        else:
            
            self.CredentialType = CredentialType(getattr(obj, 'CredentialType', None)) if getattr(obj, 'CredentialType', None) is not None else None
            self.CredentialValue = getattr(obj, 'CredentialValue', None)


