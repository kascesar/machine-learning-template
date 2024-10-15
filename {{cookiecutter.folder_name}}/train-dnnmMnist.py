"""
modulo principal de entrenamientos para el modelo **LSTM-conv-**

```shell
PYTHONPATH=. python3 train-lstmconv.py +pipeline=lstmconv-v1-datasetV1-bhp
```
"""

from {{cookiecutter.folder_name}}.train.dnnDigitMnist.pipeline import train

import hydra
from omegaconf import DictConfig


@hydra.main(version_base=None, config_path="config", config_name="config")
def main(config: DictConfig):
    train(config)


if __name__ == "__main__":
    main()
