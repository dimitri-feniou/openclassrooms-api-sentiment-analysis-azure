import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models"))

MODEL_URI = os.getenv(
    "MODEL_URI", os.path.join(BASE_DIR, "mlflow_model/LogisticRegression_model")
)
PCA_PATH = os.getenv("PCA_PATH", os.path.join(BASE_DIR, "pca_model.pkl"))
