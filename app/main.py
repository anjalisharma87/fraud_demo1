from fastapi import FastAPI
from uuid import uuid4
from .schema import LoanApp
from . import kg, model, agents

app = FastAPI(title="Fraud‑Detection KG Demo")
clf = model.load()

@app.post("/loan")
def submit(app_data: LoanApp):
    app_id = f"loan-{uuid4().hex[:8]}"
    kg.ingest_loan(app_id, app_data.dict())
    proba = clf.predict_proba([list(app_data.dict().values())])[0,1]
    agent_msg = agents.agentic_assess(app_id)
    return {
        "app_id": app_id,
        "fraud_probability": round(float(proba),4),
        "agentic_analysis": agent_msg
    }
