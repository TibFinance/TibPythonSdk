


from ..objects import FreeOperation


class CreateFreeOperationBatchArgs:
    def __init__(self, obj=None):
        if obj is None:
            
            self.SessionToken = None
            self.FreeOperationBatchList = None
            self.GroupId = None
            self.StopSameIdentifications = None

        else:
            
            self.SessionToken = getattr(obj, 'SessionToken', None)

            self.FreeOperationBatchList = []
            if hasattr(obj, 'FreeOperationBatchList') and obj.FreeOperationBatchList is not None:
                self.FreeOperationBatchList = [FreeOperation(name) for name in  obj.FreeOperationBatchList]
            self.GroupId = getattr(obj, 'GroupId', None)
            self.StopSameIdentifications = getattr(obj, 'StopSameIdentifications', None)


