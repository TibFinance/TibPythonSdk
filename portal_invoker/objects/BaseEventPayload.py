




class BaseEventPayload:
    def __init__(self, obj=None):
        if obj is None:
            
            self.EventName = None

        else:
            
            self.EventName = getattr(obj, 'EventName', None)


