import random
from .kyc import kyc_lookup

def credit_bureau_score(ssn: str) -> int:
    return random.randint(500, 850)

def kyc_check(national_id: str) -> dict:
    return kyc_lookup(national_id)
