

from .ServiceEntity import ServiceEntity


class Service(ServiceEntity):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.ServiceId = None
            self.WhiteLabelingId = None
            self.HasCompletedBoarding = None

        else:
            super().__init__(obj)

            self.ServiceId = getattr(obj, 'ServiceId', None)

            self.WhiteLabelingId = []
            if hasattr(obj, 'WhiteLabelingId') and obj.WhiteLabelingId is not None:
                self.WhiteLabelingId = [name for name in obj.WhiteLabelingId]
            self.HasCompletedBoarding = getattr(obj, 'HasCompletedBoarding', None)


