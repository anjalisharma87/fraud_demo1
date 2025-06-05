import os, json, requests
from . import kg, tools

NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY", "DUMMY_KEY")
CHAT_ENDPOINT = "https://api.nvidia.com/v1/genai/chat/completions"
HEADERS = {"Authorization": f"Bearer {NVIDIA_API_KEY}"}

SYSTEM_PROMPT = (
    "You are a fraud‑risk agent. "
    "Use supplied context triples to explain why an application might be fraudulent. "
    "If a KYC triple is missing, call the tool kyc_check. "
    "Return JSON: { 'explanation': str, 'risk': 0‑1, 'triples': list }."
)

def agentic_assess(app_id: str) -> str:
    triples_ctx = kg.query_neighbors(app_id, hops=1)
    messages = [
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":json.dumps(triples_ctx)}
    ]
    try:
        resp = requests.post(
            CHAT_ENDPOINT,
            headers=HEADERS,
            json={"model":"mixtral-8x22","messages":messages},
            timeout=10,
        )
        resp.raise_for_status()
        return resp.json()["choices"][0]["message"]["content"]
    except Exception as e:
        # fallback simple explanation
        return json.dumps({"explanation":"Fallback explanation","risk":0.5,"triples":triples_ctx})
