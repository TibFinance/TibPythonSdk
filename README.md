# TIB Finance Python SDK

![PyPI](https://img.shields.io/badge/python-3.8%2B-blue)

Python SDK for the TIB Finance payment processing API.

## Installation

```bash
git clone https://github.com/TibFinance/TibPythonSdk.git
cd TibPythonSdk
pip install .
```

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

merchant_args = GetMerchantArgs()
merchant_args.SessionToken = response.SessionId
merchant_args.MerchantId = "your_merchant_id"
merchant = Portal.getMerchant(merchant_args)
```

## Documentation

For the complete API reference and guides, visit [doc.tib.finance](https://doc.tib.finance).

This SDK provides access to **56 API methods** for payment processing, merchant management, and financial operations.

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
