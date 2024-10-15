#!/bin/bash
# Script para configurar hooks de Git

# Copiar el script de conversión y el hook de pre-commit al directorio de hooks de Git
cp hooks/convert_readme.sh .git/hooks/
cp hooks/pre-commit.sh .git/hooks/pre-commit

# Asegurarse de que los scripts sean ejecutables
chmod +x .git/hooks/convert_readme.sh
chmod +x .git/hooks/pre-commit
