#!/bin/bash
# Script de ayuda para crear el repositorio local y hacer el primer commit.
# Reemplaza <GITHUB_USERNAME> y <REPO_NAME> antes de ejecutar.

set -e

REPO_NAME="<REPO_NAME>"
GITHUB_USER="<GITHUB_USERNAME>"
REMOTE_URL="git@github.com:${GITHUB_USER}/${REPO_NAME}.git"

mkdir -p "${REPO_NAME}"
cd "${REPO_NAME}"

# Crear estructura de carpetas
mkdir -p paper notebooks data/raw data/processed data/private src/utils src/models results/modelos results/figuras

# Copiar archivos desde la carpeta /mnt/data/TFM_Repo_v0 in case user placed them there
cp /mnt/data/TFM_Repo_v0/README.md .
cp /mnt/data/TFM_Repo_v0/.gitignore .
cp /mnt/data/TFM_Repo_v0/requirements.txt .
cp /mnt/data/TFM_Repo_v0/environment.yml .

git init
git add .
git commit -m "Versión 0 - estructura inicial del proyecto"
git branch -M main

echo "Repositorio local creado. Añade el remote y push manualmente:"
echo "  git remote add origin ${REMOTE_URL}"
echo "  git push -u origin main"
