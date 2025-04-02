"""
This is a boilerplate pipeline 'classificador'
generated using Kedro 0.19.12
"""

from kedro.pipeline import node, Pipeline, pipeline  # noqa
from . import nodes

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            nodes.prepare_dataset,
            inputs=["raw_train_dev"],
            outputs="dataset_filtered",
            tags=["prepare"]
        ),
        node(
            nodes.split_dataset,
            inputs=["dataset_filtered", "params:session_id", "params:test_size"],
            outputs=["base_train", "base_test"],
            tags=["split"]
        ),
        node(
            nodes.treinamento,
            inputs=["params:model_lr", "base_train", "params:session_id"],
            outputs="treinamento_logistical_regression",
            tags=["treinamento"]
        ),
        node(
            nodes.treinamento,
            inputs=["params:model_dt", "base_train", "params:session_id"],
            outputs="treinamento_decision_tree",
            tags=["treinamento"]
        ),
        node(
            nodes.get_f1_score,
            inputs=["treinamento_logistical_regression", "base_test"],
            outputs="f1_score_metric",
            tags=["metric"]
        )
    ])
