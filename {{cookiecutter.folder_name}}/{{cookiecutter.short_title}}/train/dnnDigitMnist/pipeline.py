"""
ADD docstring here
"""

from omegaconf import DictConfig

from .steps.build_dataset import buildDS
from .steps.load_dataset import loadDS
from .steps.train import train_model


def train(config: DictConfig):
    """
    Create documentation
    """
    buildDS(config)
    dataset = loadDS(config)
    model = train_model(config, dataset)
