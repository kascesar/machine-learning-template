"""
.. include:: ../README.md
"""

import logging
import os
import warnings

import mlflow
import pandas as pd

logging.getLogger("botocore").setLevel(logging.WARNING)
logging.getLogger("boto3").setLevel(logging.WARNING)

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

warnings.filterwarnings("ignore", category=pd.errors.SettingWithCopyWarning)
warnings.filterwarnings("ignore", category=pd.errors.PerformanceWarning)
warnings.filterwarnings("ignore", category=UserWarning)

def _start_mlflow_server(uri):
    """
    Start mlflow local server
    """
    import subprocess
    mlflow_process = subprocess.Popen(
        ["mlflow", "ui", "--port", uri.split(":")[-1]], 
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return mlflow_process
    
    import requests

def _is_mlflow_running(uri):
    import requests
    try:
        response = requests.get(uri)
        return response.status_code == 200
    except requests.ConnectionError:
        return False

if os.environ.get("MLFLOW_TRACKING_URI", None):
    mlflow_uri = os.environ.get("MLFLOW_TRACKING_URI", None)
    if "localhost" in mlflow_uri:
        if not _is_mlflow_running(mlflow_uri):
            _start_mlflow_server(mlflow_uri)
            print(f"MLflow server started at : {mlflow_uri}")
        else:
            print(f"MLflow server is already running at : {mlflow_uri}")
    mlflow.set_tracking_uri(mlflow_uri)

mlflow.enable_system_metrics_logging()
mlflow.tensorflow.autolog(checkpoint_save_best_only=False)
mlflow.pytorch.autolog(checkpoint_save_best_only=False)
mlflow.sklearn.autolog()
