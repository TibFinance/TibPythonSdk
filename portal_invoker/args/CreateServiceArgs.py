


from ..objects import ServiceEntity


class CreateServiceArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.ServiceInfo = None
            self.CreateInnactive = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)
            self.ServiceInfo = ServiceEntity(getattr(obj, 'ServiceInfo', None)) if getattr(obj, 'ServiceInfo', None) is not None else None
            self.CreateInnactive = getattr(obj, 'CreateInnactive', None)


