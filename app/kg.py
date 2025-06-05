import networkx as nx

KG = nx.MultiDiGraph(name="loan_fraud_kg")

def _add_triple(sub, pred, obj):
    KG.add_edge(sub, obj, predicate=pred)

def ingest_loan(app_id: str, payload: dict):
    for k, v in payload.items():
        _add_triple(app_id, f"has_{k}", str(v))

def query_neighbors(entity: str, hops: int = 1):
    return list(nx.single_source_shortest_path_length(KG, entity, hops).keys())
