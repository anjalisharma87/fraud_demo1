import os, random

KYC_TEST_TOKEN = os.getenv("KYC_TEST_TOKEN", "TEST_TOKEN")

def kyc_lookup(national_id: str) -> dict:
    simulated_risk = round(random.uniform(0,1),2)
    return {
        "kyc_id": national_id,
        "risk_score": simulated_risk,
        "pass": simulated_risk < 0.4
    }
