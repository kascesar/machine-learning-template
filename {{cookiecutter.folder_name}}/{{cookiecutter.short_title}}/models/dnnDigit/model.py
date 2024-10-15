"""
# dnnDigit

funcitons that make the model
"""

from keras.layers import Dense, Flatten
from keras.models import Sequential
from omegaconf import DictConfig


def modelDnn(config: DictConfig) -> Sequential:
    """
    Create and return a compiled Sequential model for digit classification.

    This function constructs a simple feedforward neural network
    for classifying MNIST digits. The model consists of a Flatten
    layer followed by three Dense layers and is compiled with
    categorical crossentropy loss and the Adam optimizer.

    Returns
    -------
    Sequential
        A compiled Keras Sequential model ready for training.
    """
    model = Sequential(
        [
            Flatten(input_shape=(28, 28)),
        ]
        + [Dense(neurons) for neurons in config.pipeline.hiden_layers]
        + [
            Dense(10, activation="softmax"),
        ]
    )

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )

    return model
