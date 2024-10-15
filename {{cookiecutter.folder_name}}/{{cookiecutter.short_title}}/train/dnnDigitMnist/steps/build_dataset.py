"""
Create Dataset step
"""

from omegaconf import DictConfig


def buildDS(config: DictConfig):
    """
    Function that saves the MNIST dataset to .npy files.

    This function loads the MNIST dataset using Keras, and saves the training and testing
    images and labels into separate .npy files for later use.

    :param config: Configurations from Hydra config system, can include settings for
                   dataset management or file paths.
    :type config: DictConfig
    :return: None
    """

    from {{cookiecutter.folder_name}}.dataset.mnist.dataset import mnist_dataset

    mnist_dataset(config)
