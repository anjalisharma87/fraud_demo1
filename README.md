# 🕵️‍♂️ KG‑Powered Fraud‑Detection Demo

End‑to‑end prototype that combines:

| Pillar | Implementation |
|--------|----------------|
| **Triple‑Extraction Knowledge Graph** | In‑memory `networkx` graph updated on every loan submission |
| **Agentic AI Orchestration** | RAG‑style prompt + NVIDIA Generative AI endpoint |
| **Tool / Function Calling** | Simulated credit‑bureau & KYC look‑ups |

## Quick Start

```bash
git clone https://github.com/<your‑handle>/fraud_demo.git
cd fraud_demo
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python data/generate.py
python -c "from app import model, Path; model.train(Path('data/sample_loans.csv'))"
export NVIDIA_API_KEY=<YOUR_KEY>   # or copy .env.example → .env
uvicorn app.main:app --port 8000 &         # backend
streamlit run streamlit_app.py             # UI
```
MIT License. Fork freely!
