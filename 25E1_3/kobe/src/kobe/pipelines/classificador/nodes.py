"""
This is a boilerplate pipeline 'classificador'
generated using Kedro 0.19.12
"""

import pandas as pd

def prepare_dataset(raw_train_dev) -> pd.DataFrame:
    raw_train_dev.dropna(inplace=True)
    raw_train_dev = raw_train_dev[['lat', 'lon', 'minutes_remaining', 'period', 'playoffs', 'shot_distance', 'shot_made_flag']]
    return raw_train_dev