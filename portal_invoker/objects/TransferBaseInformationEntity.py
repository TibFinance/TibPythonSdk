




class TransferBaseInformationEntity:
    def __init__(self, obj=None):
        if obj is None:
            
            self.i = None
            self.cdt = None
            self.t = None
            self.pmt = None
            self.d = None
            self.m = None
            self.td = None
            self.a = None
            self.s = None
            self.ts = None
            self.cps = None
            self.c = None
            self.cn = None
            self.cem = None
            self.cid = None
            self.trd = None
            self.man = None
            self.map = None
            self.ed = None
            self.he = None
            self.Direction = None
            self.TransferAmount = None
            self.IsSupplierTransfer = None
            self.SupplierAlias = None
            self.ern = None

        else:
            
            self.i = getattr(obj, 'i', None)
            self.cdt = getattr(obj, 'cdt', None)
            self.t = getattr(obj, 't', None)
            self.pmt = getattr(obj, 'pmt', None)
            self.d = getattr(obj, 'd', None)
            self.m = getattr(obj, 'm', None)
            self.td = getattr(obj, 'td', None)
            self.a = getattr(obj, 'a', None)
            self.s = getattr(obj, 's', None)
            self.ts = getattr(obj, 'ts', None)
            self.cps = getattr(obj, 'cps', None)
            self.c = getattr(obj, 'c', None)
            self.cn = getattr(obj, 'cn', None)
            self.cem = getattr(obj, 'cem', None)
            self.cid = getattr(obj, 'cid', None)
            self.trd = getattr(obj, 'trd', None)
            self.man = getattr(obj, 'man', None)
            self.map = getattr(obj, 'map', None)
            self.ed = getattr(obj, 'ed', None)
            self.he = getattr(obj, 'he', None)
            self.Direction = getattr(obj, 'Direction', None)
            self.TransferAmount = getattr(obj, 'TransferAmount', None)
            self.IsSupplierTransfer = getattr(obj, 'IsSupplierTransfer', None)
            self.SupplierAlias = getattr(obj, 'SupplierAlias', None)
            self.ern = getattr(obj, 'ern', None)


