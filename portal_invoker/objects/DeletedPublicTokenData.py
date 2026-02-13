


from ..enums import DeletedPublicTokenReason


class DeletedPublicTokenData:
    def __init__(self, obj=None):
        if obj is None:
            
            self.Reason = None
            self.ReferenceData = None

        else:
            
            self.Reason = DeletedPublicTokenReason(getattr(obj, 'Reason', None)) if getattr(obj, 'Reason', None) is not None else None
            self.ReferenceData = getattr(obj, 'ReferenceData', None)


