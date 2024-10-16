"""
# Deploy

This module defines all the deployment tasks for the models. Before delving into the creation of these modules and how to organize them, it is important to consider some relevant points.

1. Each *parent* of the deployment should be the version in *camel case* format, as will be explained later.
2. Each parent version should correspond to the type of model.
3. There should only be `__init__.py` files up to the level of the dataset type.

The reason for point *3* is that the code within each version of each *deploy* must be able to function independently and should not depend on **any other module**, ensuring the correct operation of each one.

## Supported Models

| Model   |
|:-------:|
| dnnDigitMnist |
"""
