




class PendingChangeAttribute:
    def __init__(self, obj=None):
        if obj is None:
            
            self.DoNotRenderOnPublicPendingChange = None

        else:
            
            self.DoNotRenderOnPublicPendingChange = getattr(obj, 'DoNotRenderOnPublicPendingChange', None)


