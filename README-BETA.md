# TIB Finance Python SDK, beta 3.1.0b1

**Sandbox only.** Production needs the real SDK release. Do not build a production dependency on this package. `createTransferBatch`, `getTransferBatchResult` and their types can still change, and a change to them means a new beta (`b2`). Their rules are checked on the server, so a rule can change with no new package.

Install from the wheel file. It replaces any installed `tib-finance`, so use a separate virtual environment.

    pip install tib_finance-3.1.0b1-py3-none-any.whl

A first call. `ValidateOnly` checks the items and creates nothing.

```python
import uuid
from portal_invoker.api_client import set_site_url
from portal_invoker.tib_invoker import Portal
from portal_invoker.args import CreateSessionArgs, CreateTransferBatchArgs
from portal_invoker.objects import TransferBatchItem, TransferBatchCustomer, ContactInfo, Account
from portal_invoker.enums import TransferType, PaymentMethodType, Language

set_site_url("https://sandboxportal.tib.finance")

sign_in = CreateSessionArgs()
sign_in.ClientId = "your_client_id"
sign_in.Username = "your_username"
sign_in.Password = "your_password"
session = Portal.createSession(sign_in)

contact = ContactInfo()
contact.Email = "jane.doe@example.com"
contact.Phone = "5145550100"

customer = TransferBatchCustomer()
customer.CustomerExternalId = "CUST-0001"
customer.CustomerName = "Jane Doe"
customer.Language = Language.French
customer.ContactInfo = contact

account = Account()
account.Owner = "JANE DOE"
account.BankNumber = "003"
account.InstitutionNumber = "12345"
account.AccountNumber = "1234567"

item = TransferBatchItem()
item.ReferenceNumber = "REF-0001"
item.TransferType = TransferType.FreeCollection
item.PaymentMethodType = PaymentMethodType.DirectAccount
item.Amount = 125.50
item.TransactionDueDate = "2030-01-15T00:00:00"
item.Customer = customer
item.BankAccount = account

args = CreateTransferBatchArgs()
args.SessionToken = session.SessionId
args.MerchantId = "your_merchant_id"
args.IdempotencyKey = str(uuid.uuid4())
args.ValidateOnly = True
args.Items = [item]

response = Portal.createTransferBatch(args)
if response.HasError:
    print(response.Errors)
print(response.BatchOutcome)
for result in response.Results:
    print(result.Outcome, result.ErrorCode, result.Message)
```

The Python examples on the documentation pages run as written with this package.

One name differs from the pages: `CustomerAction` value 0 is `None` there and `TransferBatchCustomerAction.NotSet` here.

Documentation: https://doc.tib.finance/eng/Beta/AboutBeta
