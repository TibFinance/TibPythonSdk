
import enum

class LoginType(enum.Enum):
    NotSet = 0
    Admin = 1
    Client = 2
    Merchant = 4
    Customer = 8
    Service = 16

