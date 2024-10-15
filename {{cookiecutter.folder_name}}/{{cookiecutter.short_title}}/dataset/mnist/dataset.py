"""
Code that generete MNIS dataset
"""

import numpy as np
from omegaconf import DictConfig
from tensorflow.keras.datasets import mnist


def mnist_dataset(config: DictConfig):
    """
    Function that saves the MNIST dataset to .npy files.

    This function loads the MNIST dataset using Keras, and saves the training and testing
    images and labels into separate .npy files for later use.

    :param config: Configurations from Hydra config system, can include settings for
                   dataset management or file paths.
    :type config: DictConfig
    :return: None
    """
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    np.save(config.paths.datasets.final + "/x_train.npy", x_train)
    np.save(config.paths.datasets.final + "/y_train.npy", y_train)
    np.save(config.paths.datasets.final + "/x_test.npy", x_test)
    np.save(config.paths.datasets.final + "/y_test.npy", y_test)
    print(" * data creation done")
