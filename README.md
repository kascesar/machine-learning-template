# Artificial Inteligence Project Template

This is a [cookiecutter](https://www.cookiecutter.io/) template focused
on AI, designed for model architecture development, dataset creation,
pipeline development, and model deployment using several open and free
state-of-the-art tools.

------------------------------------------------------------------------

This project was developed with multi-model and multi-dataset studies
and implementations in mind. It is designed to use [*mlflow*](https://mlflow.org/), [*dvc*](https://dvc.org/), [*pre-commit*](https://pre-commit.com/), [*git*](https://git-scm.com/), [*docker*](https://www.docker.com/) or [*podman*](https://podman.io/), [*jupyter lab*](https://jupyter.org/), [*hydra*](https://hydra.cc/), [*bentoml*](https://www.bentoml.com/), [pipenv](https://pipenv-es.readthedocs.io), and, at your choice, various databases like *duckdb* or *PostgreSQL* in local or cloud environments.

The project manages its own environment variables through a *.env* file
integrated with *Hydra* configurations, offering two development
branches (*development* and *production*) at the *Hydra* level. The
project also uses [*pdoc*](https://pdoc.dev/) to generate useful
documentation in *HTML* format.

## Folder structure of project

```mermaid
mindmap
  markdown[Root **folder_name**]
    markdown[**configs**]
      database
        duckdb
        mysql
        postgres
        sqlite
      mlflow
        development_mlflow
        production_mlflow
      optuna
        development_optuna
        production_optuna
      pipeline
        modelv1
      type
        development_type
        production_type
    markdown[Source **short_title**]
      markdown[**datasets**]
        datasetV1
      markfown[**deploy**]
        modelV1_deploy
          docker
      markdown[**models**]
        modelexample
          notebooks
      markdown[**train**]
        trainV1
          steps
    dataset
      final
      processed
      raw
    docs
```

## Requeriments (Linux - debian like OS)

This project takes care of configuring all its dependencies and tools.
However, it requires that you have the Python package manager (*pip*)
and *cookiecutter* installed.

```shell
sudo apt install python3-pip git && \
pip install --upgrade pip && \
pip install --upgrade cookiecutter
```

## recomended configurations

there is two options that are recomended
1. On project folder python envioriment
2. git default branch as main

```shell
export PIPENV_VENV_IN_PROJECT=1
git config --global init.defaultBranch main
```


## Instantiate a projet

To instantiate a project, you can do it just typing

```shell
cookiecutter https://github.com/kascesar/artificial-inteligence-template.git
```

then follow the instruction.git

---

## For developers - Configure git hooks for this project

after *cloning*

```shell
chmod +x setup_hooks.sh && \
sh setup_hooks.sh
```

---

# Read before using

## Who might find this template useful?

**R**: Anyone, whether a developer, data scientist, or machine learning engineer, who wants to have a clean, simple, scalable, and replicable development environment.



## Who is this template designed for?

**R**: For developers using free and/or open-source MLOps and artificial intelligence tools like mlflow, optuna, bentoml, docker, tensorflow, etc ...  aimed at studying, developing, and deploying models to production.

## What knowledge do I need to use this template?

**R**: At least have a moderate understanding of Python, MLflow, DVC, Git, and Hydra.
