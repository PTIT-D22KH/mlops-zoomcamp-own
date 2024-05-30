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
    mlflow.set_tracking_uri("http://mlflow:5000")
    # mlflow.list_experiments()
    # print(mlflow.list_experiments())
    
    mlflow.set_experiment("log_model")
    dv, lr = data[0], data[1]

    with mlflow.start_run():    
        mlflow.sklearn.log_model(lr, artifact_path="models")