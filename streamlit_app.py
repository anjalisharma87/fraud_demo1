import json, requests, streamlit as st
from pyvis.network import Network
import networkx as nx

BACKEND_URL = "http://localhost:8000/loan"
st.set_page_config(page_title="Loan Fraud Demo", page_icon="🕵️‍♂️")
st.title("🕵️‍♂️ Loan Fraud Detection – KG + Agentic AI")

with st.sidebar:
    st.header("Applicant Data")
    loan_amount = st.number_input("Loan amount ($)", 1000, 50000, 12000)
    term_months = st.selectbox("Term (months)", [24,36,48,60], 1)
    credit_score = st.slider("Credit score", 300, 850, 710)
    income = st.number_input("Annual income ($)", 10000, 200000, 85000)
    age = st.slider("Age", 18, 70, 29)
    dti = st.slider("Debt‑to‑Income ratio", 0.0, 1.0, 0.21)
    default_prev = st.checkbox("Previous default?")
    if st.button("Submit"):
        payload = {
            "loan_amount": loan_amount,
            "term_months": term_months,
            "credit_score": credit_score,
            "income": income,
            "age": age,
            "debt_to_income_ratio": dti,
            "has_previous_default": int(default_prev),
        }
        with st.spinner("Calling backend…"):
            r = requests.post(BACKEND_URL, json=payload, timeout=10)
        if r.ok:
            resp = r.json()
            st.success(f"Fraud probability: **{resp['fraud_probability']*100:.1f}%**")
            st.write("### Agentic Analysis")
            st.json(json.loads(resp["agentic_analysis"]))
            # show KG if triples present
            triples = json.loads(resp["agentic_analysis"]).get("triples", [])
            if triples:
                g = nx.MultiDiGraph()
                for s,p,o in triples:
                    g.add_edge(s,o,label=p)
                net = Network(height="400px", directed=True)
                net.from_nx(g)
                net.show("kg.html")
                with open("kg.html") as f:
                    st.components.v1.html(f.read(), height=420)
        else:
            st.error(r.text)
