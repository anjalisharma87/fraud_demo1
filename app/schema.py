from pydantic import BaseModel, confloat, conint

class LoanApp(BaseModel):
    loan_amount: confloat(gt=0)
    term_months: conint(gt=0)
    credit_score: conint(ge=300, le=850)
    income: confloat(gt=0)
    age: conint(ge=18)
    debt_to_income_ratio: confloat(ge=0, le=1)
    has_previous_default: conint(ge=0, le=1)
