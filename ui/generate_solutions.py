import json
import os

# Transforma o arquivo JSON em dicionario e pega a lista de soluções
with open("solutions.json") as f:
    solutions = json.load(f)
    solutions = solutions["questions_userlog"]

# Passa as soluções para arquivos python separados
# Itera pelas soluções, pegando o indice e o código
for i, solution in enumerate(solutions):
    # Define o nome do arquivo
    filename = f"solution{i}.py"
    with open(filename, 'w') as f:
        f.write(solution["solution"])
