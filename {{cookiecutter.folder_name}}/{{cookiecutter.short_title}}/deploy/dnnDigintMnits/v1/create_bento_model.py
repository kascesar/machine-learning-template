"""
This code make the bento model
**NOTA**: This mudule must be executed lonely
"""

import bentoml

_model_uri = 'runs:/fee78963f20c4cd2835d18d78ae7aca4/model'
bentoml.mlflow.import_model(
    "dnn-clf-mnist",
    model_uri=_model_uri,
    signatures={"predict": {"batchable": True, "batch_dim": 0}},
)

