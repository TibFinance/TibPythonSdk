
import enum

class BoardingDocType(enum.Enum):
    unknown = -1
    notSet = 0
    companyIdentificationProof = 1
    bankAccountIdentificationProof = 2
    person1IdentificationProof = 3
    person2IdentificationProof = 4
    shareholder1IdentificationProof = 5
    shareholder2IdentificationProof = 6
    shareholder3IdentificationProof = 7
    shareholder4IdentificationProof = 8

