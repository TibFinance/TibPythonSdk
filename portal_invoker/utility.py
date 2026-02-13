import json
import re
from enum import Enum


def object2dict(model):
    if not hasattr(model, "__dict__"):
        return model
    if isinstance(model, Enum):
        return model.value
    result = {}
    for key, val in model.__dict__.items():
        if key.startswith("_"):
            key = key.replace("_", "")
        element = []
        if isinstance(val, list):
            for item in val:
                element.append(object2dict(item))
        else:
            element = object2dict(val)
        result[key] = element
    return result


class Obj:
    # constructor
    def __init__(self, dict1):
        self.__dict__.update(dict1)


def dict2obj(dict1):
    # using json.loads method and passing json.dumps
    # method and custom object hook as arguments
    return json.loads(json.dumps(dict1), object_hook=Obj)


REGEX_MAPPER = {
    "NAME_VALIDATION": r"^[A-Za-z0-9_ -@.,'!?;:&$%*()àâçéèêëîïôûùüÿñæœ]{1,150}$",
    "DESCRIPTION_VALIDATION": r"^[A-Za-z0-9_ -@.,'!?;:&$%*()àâçéèêëîïôûùüÿñæœ]{0,150}$",
    "INTERAC_DESCRIPTION_VALIDATION": r"^[A-Za-z0-9_ -@.,'!?;:&$%*()àâçéèêëîïôûùüÿñæœ]{1,140}$",
    "BANK_NUMBER_VALIDATION": r"^[0-9]{1,3}$",
    "INSTITUTION_NUMBER_VALIDATION": r"^[0-9]{1,5}$",
    "ACCOUNT_NUMBER_VALIDATION": r"^[0-9]{1,15}$",
    "CARD_OWNER_VALIDATION": r"^[a-zA-Z0-9 -]{1,150}$",
    "PAN_VALIDATION": r"^[0-9]{14,16}$",
    "EXPIRATION_MONTH_VALIDATION": r"^(0?[1-9]|1[012])$",
    "EXPIRATION_YEAR_VALIDATION": r"^[1-9][0-9]?$",
    "CVD_VALIDATION": r"^[0-9]{14,16}$",
    "STREET_ADDRESS_VALIDATION": r"^[A-Za-z0-9_ -@.,'!?;:&$%*()àâçéèêëîïôûùüÿñæœ]{1,250}$",
    "CITY_VALIDATION": r"^[A-Za-z0-9 -àâçéèêëîïôûùüÿñæœ]{1,140}$",
    "UUID_VALIDATION": r"^[0-9a-fA-F]{8}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{4}\-[0-9a-fA-F]{12}$",
    "BILL_DESCRIPTION_VALIDATION": r"^[A-Za-z0-9_ -@.,'!?;:&$%*()àâçéèêëîïôûùüÿñæœ]{1,1000}$",
    "INTERAC_OWNER_VALIDATION": r"^[A-Za-z0-9,_@. àâçéèêëîïôûùüÿñæœ]{1,80}$",
    "EMAIL_VALIDATION": r"^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$",
    "MOBILE_VALIDATION": r"^[0-9-]{10}$",
    "INTERAC_QUESTION_VALIDATION": r"^[A-Za-z0-9_@., 'àâçéèêëîïôûùüÿñæœ]{1,40}$",
    "INTERAC_ANSWER_VALIDATION": r"^[A-Za-z0-9 -'àâçéèêëîïôûùüÿñæœ]{1,40}$",
    "MERCHANT_ACCOUNT_NAME_VALIDATION": r"^[A-Za-z0-9 'àâçéèêëîïôûùüÿñæœ]{1,15}$",
    "MERCHANT_PHONE_VALIDATION": r"^[0-9 -]{1,150}$"
}


def validate_field(regex_key, value):
    r = REGEX_MAPPER[regex_key]
    regex = re.compile(r)
    match = regex.match(str(value))
    return bool(match)
