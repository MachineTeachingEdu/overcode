#!/bin/sh
set -e  # Interrompe o script se houver erro

# Path para os dados de soluções dos alunos
TARGET_PATH="${PWD}/ui"
FUNCTION_NAME="posLetra"

# Executa as soluções dos alunos
python src/run_pipeline.py $TARGET_PATH --run-pre -n $FUNCTION_NAME

# Executa a análise das soluções
python src/run_pipeline.py $TARGET_PATH --run-pipeline -d

# Roda o servidor da interface
cd ./ui
./runServer.sh