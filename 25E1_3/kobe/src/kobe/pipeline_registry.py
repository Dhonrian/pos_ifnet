"""Project pipelines."""
from __future__ import annotations

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
import kobe.pipelines.data_prep as data_prep
import kobe.pipelines.training as training
import kobe.pipelines.application as application


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    #pipelines = find_pipelines()
    #pipelines["__default__"] = sum(pipelines.values())
    #return pipelines

    data_prep_pipeline = data_prep.create_pipeline()
    training_pipeline = training.create_pipeline()
    application_pipeline = application.create_pipeline()
    

    return {
        "__default__": data_prep_pipeline + training_pipeline + application_pipeline,
        "data_prep": data_prep_pipeline,
        "training": training_pipeline,
        "application": application_pipeline,
    }