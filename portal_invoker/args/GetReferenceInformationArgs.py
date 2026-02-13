


from ..enums import GetReferenceInformationType


class GetReferenceInformationArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ReferenceData = None
            self.ReferenceInformationType = None

        else:
            
            self.ReferenceData = getattr(obj, 'ReferenceData', None)
            self.ReferenceInformationType = GetReferenceInformationType(getattr(obj, 'ReferenceInformationType', None)) if getattr(obj, 'ReferenceInformationType', None) is not None else None


