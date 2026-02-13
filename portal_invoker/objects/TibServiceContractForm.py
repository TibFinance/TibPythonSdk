


from ..enums import Language


class TibServiceContractForm:
    def __init__(self, obj=None):
        if obj is None:
            
            self.BankName = None
            self.BankAddress = None
            self.BankCity = None
            self.BankProvince = None
            self.BankCountry = None
            self.BankName1 = None
            self.BankNumber1 = None
            self.BankTransit1 = None
            self.BankAccount1 = None
            self.EnterpriseName = None
            self.OwnerName = None
            self.OwnerAddress = None
            self.OwnerCity = None
            self.OwnerCountry = None
            self.OwnerProvince = None
            self.OwnerPostalCode = None
            self.OwnerEmail = None
            self.TransactionNumberWithdraw = None
            self.TransactionNumberDeposit = None
            self.TransactionNumberNsf = None
            self.AmountLimitWithdraw = None
            self.AmountLimitDeposit = None
            self.AmountLimitNsf = None
            self.transactionMaxAmount = None
            self.autorizationMail1 = None
            self.autorizationMail2 = None
            self.DoubleAuthenticationAccount = None
            self.authorizationLimit = None
            self.clientAutorisationLimit = None
            self.IsAccepted = None
            self.PublicToken = None
            self.DefaultCustomerLanguage = None

        else:
            
            self.BankName = getattr(obj, 'BankName', None)
            self.BankAddress = getattr(obj, 'BankAddress', None)
            self.BankCity = getattr(obj, 'BankCity', None)
            self.BankProvince = getattr(obj, 'BankProvince', None)
            self.BankCountry = getattr(obj, 'BankCountry', None)
            self.BankName1 = getattr(obj, 'BankName1', None)
            self.BankNumber1 = getattr(obj, 'BankNumber1', None)
            self.BankTransit1 = getattr(obj, 'BankTransit1', None)
            self.BankAccount1 = getattr(obj, 'BankAccount1', None)
            self.EnterpriseName = getattr(obj, 'EnterpriseName', None)
            self.OwnerName = getattr(obj, 'OwnerName', None)
            self.OwnerAddress = getattr(obj, 'OwnerAddress', None)
            self.OwnerCity = getattr(obj, 'OwnerCity', None)
            self.OwnerCountry = getattr(obj, 'OwnerCountry', None)
            self.OwnerProvince = getattr(obj, 'OwnerProvince', None)
            self.OwnerPostalCode = getattr(obj, 'OwnerPostalCode', None)
            self.OwnerEmail = getattr(obj, 'OwnerEmail', None)
            self.TransactionNumberWithdraw = getattr(obj, 'TransactionNumberWithdraw', None)
            self.TransactionNumberDeposit = getattr(obj, 'TransactionNumberDeposit', None)
            self.TransactionNumberNsf = getattr(obj, 'TransactionNumberNsf', None)
            self.AmountLimitWithdraw = getattr(obj, 'AmountLimitWithdraw', None)
            self.AmountLimitDeposit = getattr(obj, 'AmountLimitDeposit', None)
            self.AmountLimitNsf = getattr(obj, 'AmountLimitNsf', None)
            self.transactionMaxAmount = getattr(obj, 'transactionMaxAmount', None)
            self.autorizationMail1 = getattr(obj, 'autorizationMail1', None)
            self.autorizationMail2 = getattr(obj, 'autorizationMail2', None)
            self.DoubleAuthenticationAccount = getattr(obj, 'DoubleAuthenticationAccount', None)
            self.authorizationLimit = getattr(obj, 'authorizationLimit', None)
            self.clientAutorisationLimit = getattr(obj, 'clientAutorisationLimit', None)
            self.IsAccepted = getattr(obj, 'IsAccepted', None)
            self.PublicToken = getattr(obj, 'PublicToken', None)
            self.DefaultCustomerLanguage = Language(getattr(obj, 'DefaultCustomerLanguage', None)) if getattr(obj, 'DefaultCustomerLanguage', None) is not None else None


