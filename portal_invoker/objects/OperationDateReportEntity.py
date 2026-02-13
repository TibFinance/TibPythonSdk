


from ..enums import OperationCategoryReportType


class OperationDateReportEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.ReportDate = None
            self.Categories = None

        else:
            
            self.ReportDate = getattr(obj, 'ReportDate', None)

            self.Categories = []
            if hasattr(obj, 'Categories') and obj.Categories is not None:
                self.Categories = [OperationCategoryReportType(name) for name in  obj.Categories]


