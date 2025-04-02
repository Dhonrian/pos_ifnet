"""
This is a boilerplate pipeline 'classificador'
generated using Kedro 0.19.12
"""

import pandas as pd
from pycaret.classification import ClassificationExperiment 
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score
from kedro_mlflow.io import MlflowMetricDataset
import mlflow

def prepare_dataset(raw_train_dev) -> pd.DataFrame:
    raw_train_dev.dropna(inplace=True)
    raw_train_dev = raw_train_dev[['lat', 'lon', 'minutes_remaining', 'period', 'playoffs', 'shot_distance', 'shot_made_flag']]
    return raw_train_dev

def split_dataset(dataset_filtered, session_id, test_size) -> pd.DataFrame:
    train, test = train_test_split(dataset_filtered, test_size=test_size, random_state=session_id, stratify=dataset_filtered['shot_made_flag'])

    with mlflow.start_run(run_name="split information", nested=True):
        mlflow.log_param("test_size", test_size)
        mlflow.log_metric("train_size", len(train))
        mlflow.log_metric("test_size", len(test))
   
    return train, test


def treinamento_best_model(base_train, session_id) -> ClassificationExperiment:
    exp = ClassificationExperiment()
    exp.setup(data=base_train, target='shot_made_flag', session_id=session_id, use_gpu=True)
    best_model = exp.compare_models(sort='f1')
    return best_model

def treinamento(model_name, base_train, session_id) -> ClassificationExperiment:
    """
    Train model and register in MLFlow
    Args:
        model_name (str): Name of the model to train ('dt', 'lr').
        base_train (pd.DataFrame): Training dataset.
        session_id (int): Session ID for PyCaret.
    """
    exp = ClassificationExperiment()
    exp.setup(data=base_train, target='shot_made_flag', session_id=session_id, use_gpu=True, log_experiment=True, experiment_name="kobe") 
    
    with mlflow.start_run(run_name=f"Training_{model_name}", nested=True):
        mlflow.log_param("model_name", model_name)

        model = exp.create_model(model_name)

        exp.tune_model(model, n_iter=10, optimize='f1')

        metrics = exp.get_metrics()
        f1_score = metrics.get("F1 Score", None)
        
        if f1_score is not None:
            mlflow.log_metric("f1_score", f1_score)
    return model


def get_f1_score(model, base_test):

    predictions = model.predict(base_test.drop(columns=['shot_made_flag']))
    
    y_true = base_test['shot_made_flag']
    f1 = f1_score(y_true, predictions)

    metric_ds = MlflowMetricDataset(key="f1_score")
    metric_ds.save({"f1_score": f1})
    
    with mlflow.start_run(run_name="F1_Score_Calculation"):
        mlflow.log_metric("f1_score", f1)
