import os
import pickle
import click

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

import mlflow


mlflow.set_tracking_uri("sqlite:///mlflow.db")
mlflow.set_experiment("nyc-taxi-experiment")

def load_pickle(filename: str):
    with open(filename, "rb") as f_in:
        return pickle.load(f_in)


@click.command()
@click.option(
    "--data_path",
    default="./output",
    help="Location where the processed NYC taxi trip data was saved"
)
def run_train(data_path: str):
    X_train, y_train = load_pickle(os.path.join(data_path, "train.pkl"))
    X_val, y_val = load_pickle(os.path.join(data_path, "val.pkl"))
    rf = RandomForestRegressor(max_depth=10, random_state=0)
    rf.fit(X_train, y_train)
    y_pred = rf.predict(X_val)
    with open('/workspaces/mlops-zoomcamp-own/02-experiment-tracking/hw/models/hw_rf.bin', 'wb') as f_out:
        pickle.dump(rf, f_out)
    with mlflow.start_run():
        mlflow.set_tag("developer", "duongvct");
        mlflow.log_param("train-data-path", "/workspaces/mlops-zoomcamp-own/02-experiment-tracking/hw/output/train.pkl")
        mlflow.log_param("valid-data-path", "/workspaces/mlops-zoomcamp-own/02-experiment-tracking/hw/output/val.pkl")
        

        rf = RandomForestRegressor(max_depth=10, random_state=0)
        rf.fit(X_train, y_train)
        y_pred = rf.predict(X_val)
        mlflow.log_param("min_samples_split", rf.get_params()['min_samples_split'])
        rmse = mean_squared_error(y_val, y_pred, squared=False)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_artifact(local_path = '/workspaces/mlops-zoomcamp-own/02-experiment-tracking/hw/models/hw_rf.bin', artifact_path = 'models_pickle')



if __name__ == '__main__':
    run_train()
