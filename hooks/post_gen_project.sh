#!/bin/bash

export PIPENV_VENV_IN_PROJECT=1
git config --global init.defaultBranch main
git init
pipenv install
pipenv run dvc init
pipenv run dvc config core.analytics false
.venv/bin/pre-commit install
pipenv run pdoc --mermaid --math {{cookiecutter.folder_name}}/ -o docs/
git add .
git commit -m "Project {{cookiecutter.short_title}} creation"
git add .
git commit -m "Project {{cookiecutter.short_title}} creation"
