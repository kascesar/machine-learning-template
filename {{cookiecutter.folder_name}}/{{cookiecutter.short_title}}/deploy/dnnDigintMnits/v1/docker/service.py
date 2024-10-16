from io import StringIO
import numpy as np
import bentoml
import pandas as pd
from bentoml.io import JSON, Text

model_ref = bentoml.mlflow.get("dnn-clf-mnist:latest")
runner = model_ref.to_runner()

svc = bentoml.Service(
    name="dnn-clf-mnist",
    runners=[runner],
)

sample_input = [
    [np.random.randint(0, 256) for _ in range(28 * 28)] for _ in range(5)
]

@svc.api(input=Text.from_sample(sample_input), output=JSON())
async def predict(data):
    data_list = eval(data)
    data_df = pd.DataFrame(data_list)
    X, dts = xbuilder(data_df)
    result = await runner.async_run(X)
    return {
        "anomaly-score": [f"{i}" for i in mesure(X, result)],
        "timestamp": dts
    }
