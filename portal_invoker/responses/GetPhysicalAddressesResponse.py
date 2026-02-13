

from .BaseApiResponse import BaseApiResponse


class GetPhysicalAddressesResponse(BaseApiResponse):
    def __init__(self, obj=None):
        if obj is None:
            super().__init__()
            self.Countries = None
            self.Provinces = None

        else:
            super().__init__(obj)
            if not obj.HasError:

                self.Countries = []
                if hasattr(obj, 'Countries') and obj.Countries is not None:
                    self.Countries = [name for name in obj.Countries]

                self.Provinces = []
                if hasattr(obj, 'Provinces') and obj.Provinces is not None:
                    self.Provinces = [name for name in obj.Provinces]


