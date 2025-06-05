import pandas as pd, numpy as np, pathlib

def synth(n=5_000, seed=42):
    rng = np.random.default_rng(seed)
    rows = []
    for _ in range(n):
        cs = rng.integers(500, 830)
        dti = rng.random()
        fraud = int((cs < 600 and dti > 0.35) or rng.random() < 0.05)
        rows.append({
            "loan_amount": rng.integers(5_000, 30_000),
            "term_months": rng.choice([24,36,48,60]),
            "credit_score": cs,
            "income": rng.integers(30_000, 120_000),
            "age": rng.integers(21,65),
            "debt_to_income_ratio": round(dti,2),
            "has_previous_default": rng.integers(0,2),
            "is_fraud": fraud,
        })
    df = pd.DataFrame(rows)
    path = pathlib.Path(__file__).parent / "sample_loans.csv"
    df.to_csv(path, index=False)
    print("✅  Sample dataset written to", path)

if __name__ == "__main__":
    synth()
