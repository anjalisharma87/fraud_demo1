import joblib, pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

MODEL_FILE = Path(__file__).parent.parent / "fraud_model.joblib"

def train(csv_path: Path):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=["is_fraud"])
    y = df["is_fraud"]
    Xtr, Xtst, ytr, ytst = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)
    pipe = Pipeline([("scale", StandardScaler()), ("clf", LogisticRegression(max_iter=1000))])
    pipe.fit(Xtr, ytr)
    joblib.dump(pipe, MODEL_FILE)
    return pipe.score(Xtst, ytst)

def load():
    return joblib.load(MODEL_FILE)
