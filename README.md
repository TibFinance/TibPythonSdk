# TIB Finance Python SDK

![PyPI](https://img.shields.io/badge/python-3.8%2B-blue)

Python SDK for the TIB Finance payment processing API.

## Installation

```bash
git clone https://github.com/TibFinance/TibPythonSdk.git
cd TibPythonSdk
pip install .
```

Alternatively, download the prebuilt wheel (`.whl`) from the latest [GitHub release](https://github.com/TibFinance/TibPythonSdk/releases) and install it with `pip install <file>.whl`.

## Quick Start

```python
from portal_invoker.api_client import set_site_url
from portal_invoker.tib_invoker import Portal
from portal_invoker.args import CreateSessionArgs, GetMerchantArgs

set_site_url("https://sandboxportal.tib.finance")

session_args = CreateSessionArgs()
session_args.ClientId = "your_client_id"
session_args.Username = "your_username"
session_args.Password = "your_password"
response = Portal.createSession(session_args)

# Always check the error flag before using the response payload
if response.HasError:
    print("Session failed:", response.Messages)
else:
    merchant_args = GetMerchantArgs()
    merchant_args.SessionToken = response.SessionId
    merchant_args.MerchantId = "your_merchant_id"
    merchant = Portal.getMerchant(merchant_args)
```

## Two-step sign-in (merchant- or service-level users)

The Quick Start signs in with `Portal.createSession`, which opens a client-level session. A user whose access is limited to a merchant or a service signs in with two calls instead:

1. Call `Portal.getLoginAccessList` with the client ID, username and password. Each entry in `LoginRelations` is one access the user can open: `InternalReferenceType` gives its level (2 client, 4 merchant, 16 service) and `InternalReferenceId` the ID of that client, merchant or service. `Description` is a label for display only.
2. Call `Portal.login` with the same client ID, username and password, and the `LoginsUserRelationsId` of the chosen entry.

Send the returned `SessionId` as `SessionToken` on the following calls, as with `Portal.createSession`. Failed sign-in attempts count toward a temporary lockout, so do not retry in a loop.

```python
from portal_invoker.tib_invoker import Portal
from portal_invoker.args import GetLoginAccessListArgs, LoginArgs, ListServicesArgs

list_args = GetLoginAccessListArgs()
list_args.ClientId = "your_client_id"
list_args.Username = "your_username"
list_args.Password = "your_password"
accesses = Portal.getLoginAccessList(list_args)
if accesses.HasError:
    print("Sign-in failed:", accesses.Messages)
else:
    # Each entry is one access: pick the one to open
    # (InternalReferenceType: 2 client, 4 merchant, 16 service).
    access = accesses.LoginRelations[0]

    login_args = LoginArgs()
    login_args.ClientId = "your_client_id"
    login_args.Username = "your_username"
    login_args.Password = "your_password"
    login_args.LoginsUserRelationsId = access.LoginsUserRelationsId
    response = Portal.login(login_args)
    if response.HasError:
        print("Sign-in failed:", response.Messages)
    else:
        services_args = ListServicesArgs()
        services_args.SessionToken = response.SessionId
        services = Portal.listServices(services_args)
```

## Documentation

For the complete API reference and guides, visit [doc.tib.finance](https://doc.tib.finance).

This SDK provides access to **67 API methods** for payment processing, merchant management, and financial operations.

## Other TIB Finance SDKs

| SDK | Repository |
|-----|------------|
| Java | [TibJavaSdk](https://github.com/TibFinance/TibJavaSdk) |
| .NET Core | [TibDotNetCoreSdk](https://github.com/TibFinance/TibDotNetCoreSdk) |
| .NET Framework | [TibDotNetSdk](https://github.com/TibFinance/TibDotNetSdk) |
| PHP | [TibPhpSdk](https://github.com/TibFinance/TibPhpSdk) |
| JavaScript (Browser) | [TibJavascriptSdk](https://github.com/TibFinance/TibJavascriptSdk) |
| Node.js | [TibNodeJsSdk](https://github.com/TibFinance/TibNodeJsSdk) |

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support

- Documentation: [doc.tib.finance](https://doc.tib.finance)
- Email: support@tib.finance
