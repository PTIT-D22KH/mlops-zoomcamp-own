import mlflow
from mlflow import sklearn
import pickle

@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exports data to some source.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Output (optional):
        Optionally return any object and it'll be logged and
        displayed when inspecting the block run.
    """
    # Assume that `data` is a tuple containing the DictVectorizer and the model
    vectorizer, model = data

    with mlflow.start_run():
        sklearn.log_model(model, "model")
        with open("vectorizer.pkl", "wb") as f:
            pickle.dump(vectorizer, f)
        mlflow.log_artifact("vectorizer.pkl")