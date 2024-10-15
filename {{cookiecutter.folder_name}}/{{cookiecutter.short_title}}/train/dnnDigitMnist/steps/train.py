"""
# Train Step Module

This module contains functions related to the training of machine learning models.
It includes the `train` function that facilitates the training of a model using 
a provided dataset. The function trains the model on the training set and evaluates 
its performance on the test set, printing the results.

Modules
-------
- train: Contains the `train` function to train the model.
"""

from omegaconf import DictConfig


def train_model(config: DictConfig, dataset):
    """
    Train the provided model on the given dataset.

    This function takes a dataset tuple containing training and testing data,
    trains the model using the training data, and optionally evaluates it on
    the test data.

    :param dataset: A tuple containing the training images, training labels,
                    testing images, and testing labels.
    :type dataset: Tuple[array, array, array, array]
    :param model: The model to be trained. It should have a `train` method that
                  accepts training data and labels.
    :type model: Any model object with a `train` method
    :return: None
    """

    from {{cookiecutter.folder_name}}.models.dnnDigit.model import modelDnn

    model = modelDnn(config)
    x_train, y_train, x_test, y_test = dataset

    model.fit(
        x_train,
        y_train,
        epochs=config.pipeline.epochs,
        batch_size=config.pipeline.epochs,
        validation_data=(x_test, y_test),
    )

    test_loss, test_accuracy = model.evaluate(x_test, y_test)

    print(f"Test loss: {test_loss}, Test accuracy: {test_accuracy}")
    return model
