#!/bin/bash

export PIPENV_VENV_IN_PROJECT=1
git config --global init.defaultBranch main
git init
pipenv install
dvc init
dvc config core.analytics false
pre-commit install
git add .
pipenv run pdoc --mermaid --math {{cookiecutter.folder_name}}/ -o docs/
git commit -m "Project {{cookiecutter.short_title}} creation"
git add .
git commit -m "Project {{cookiecutter.short_title}} creation"
