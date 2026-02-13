




class AcpAccount:
    def __init__(self, obj=None):
        if obj is None:
            
            self.OrganizationNumber = None
            self.OrganizationName = None
            self.OrganizationAccount = None
            self.OrganizationBank = None
            self.OrganizationShortName = None
            self.RoutingInformation = None

        else:
            
            self.OrganizationNumber = getattr(obj, 'OrganizationNumber', None)
            self.OrganizationName = getattr(obj, 'OrganizationName', None)
            self.OrganizationAccount = getattr(obj, 'OrganizationAccount', None)
            self.OrganizationBank = getattr(obj, 'OrganizationBank', None)
            self.OrganizationShortName = getattr(obj, 'OrganizationShortName', None)
            self.RoutingInformation = getattr(obj, 'RoutingInformation', None)


