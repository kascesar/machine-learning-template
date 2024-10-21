import hydra
from omegaconf import DictConfig
from hydra.utils import instantiate


@hydra.main(config_path="config", config_name="config")
def main(config: DictConfig):
    db = instantiate(config.database)
    session = db()
    """This is an sqlalchemy database session"""


if __name__ == "__main__":
    main()
