"""
Step that load mnist dataset
"""

from typing import Tuple

import numpy as np
from omegaconf import DictConfig


def loadDS(config: DictConfig) -> Tuple[np.array, np.array, np.array, np.array]:
    """
    Load and return the MNIST dataset instances from specified paths.

    This function loads the MNIST dataset from the paths defined in the Hydra configuration,
    normalizes the pixel values to the range [0, 1], and converts the labels to a one-hot
    encoded format. The function returns the training and testing datasets as arrays.

    :param config: Configuration object from Hydra containing paths to the dataset files.
    :type config: DictConfig
    :return: A tuple containing the training images, training labels, testing images,
             and testing labels as arrays.
    :rtype: Tuple[array, array, array, array]
    """
    x_train = np.load(config.paths.datasets.final + "/x_train.npy")
    y_train = np.load(config.paths.datasets.final + "/y_train.npy")
    x_test = np.load(config.paths.datasets.final + "/x_test.npy")
    y_test = np.load(config.paths.datasets.final + "/y_test.npy")

    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0
    print("* load dataset complete")
    return (x_train, y_train, x_test, y_test)
