"""
This is a boilerplate pipeline 'classificador'
generated using Kedro 0.19.12
"""

import pandas as pd
from pycaret.classification import ClassificationExperiment 
import mlflow

def prepare_dataset(raw_train_dev) -> pd.DataFrame:
    raw_train_dev.dropna(inplace=True)
    raw_train_dev = raw_train_dev[['lat', 'lon', 'minutes_remaining', 'period', 'playoffs', 'shot_distance', 'shot_made_flag']]
    return raw_train_dev

def treinamento_best_model(dataset_filtered, session_id) -> ClassificationExperiment:
    exp = ClassificationExperiment()
    exp.setup(data=dataset_filtered, target='shot_made_flag', session_id=session_id, use_gpu=True, log_experiment='mlflow', experiment_name='kobe')
    best_model = exp.compare_models(sort='f1')
    return best_model