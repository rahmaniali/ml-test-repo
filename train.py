import sys
import os
from mlflow import log_metric, log_param, log_artifact
import mlflow


alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 2

with mlflow.start_run():

    rmse = myfunc(5)


    mlflow.log_param("alpha", alpha)
    mlflow.log_param("l1_ratio", l1_ratio)
    mlflow.log_metric("rmse", rmse)
