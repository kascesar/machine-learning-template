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

---

## User Flow

```mermaid
C4Context
    title Process of Model Logging and Dockerization

    Enterprise_Boundary(b0, "ML System") {
        Person(User, "User", "Initiates the model logging and dockerization process.")
        
        System(MLflow, "MLflow", "Tracks and registers machine learning models.")
        
        Enterprise_Boundary(b1, "Bento System") {

            System(Script, "create_bento_file.py", "Script that generates the Bento model or runner.")
            
            System_Ext(Docker, "Docker", "Containerizes the Bento model.")
        }
    }

    Rel(User, MLflow, "Logs the model in")
    Rel(User, Script, "Executes the script")
    Rel(Script, Docker, "Containerizes the Bento model")
    Rel(Docker, User, "Confirms containerization")

    UpdateElementStyle(User, $fontColor="black", $bgColor="#FFEB3B", $borderColor="black")
    UpdateRelStyle(User, MLflow, $textColor="blue", $lineColor="blue")
    UpdateRelStyle(User, Script, $textColor="green", $lineColor="green")
    UpdateRelStyle(Script, Docker, $textColor="orange", $lineColor="orange")
    UpdateRelStyle(Docker, User, $textColor="purple", $lineColor="purple")

```
"""
