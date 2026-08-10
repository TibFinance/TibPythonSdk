

from .ServiceEntity import ServiceEntity


class Service(ServiceEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ServiceId = None
            self.HasCompletedBoarding = None

        else:
            super().__init__(obj)
            self.ServiceId = getattr(obj, 'ServiceId', None)
            self.HasCompletedBoarding = getattr(obj, 'HasCompletedBoarding', None)


