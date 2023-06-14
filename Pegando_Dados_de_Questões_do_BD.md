# Pegando Dados de Questões do BD do Machine Teaching

## 0. Criar um banco de dados no SQLite

Guarde as informações como nome do BD, nome de usuário e senha, além do host e porta do BD.

## 1. Clonar o repositório do Machine Teaching

https://github.com/MachineTeachingEdu/machine-teaching.git

## 2. Baixar o arquivo JSON do BD (procurar links no Discord)

O nome do arquivo deve ser `db_2022_05_16.tar.gz` e deve estar disponível para download pelo DropBox.

Por enquanto, apenas faça a descompressão e deixe o arquivo `db_2022_05_16.json` (ou o equivalente) na pasta `machineteaching` do projeto.

## 3. Copiar .env.example para .env

Na pasta `machineteaching` do projeto, execute:
```
cp .env.example .env
```

Preencher com os dados de acesso ao banco de dados e dados para o Django. Exemplo:

```
DB_ENGINE="django.db.backends.sqlite3"
DB_NAME=nome_bd
DB_USER=nome_usuario
DB_PASSWORD=senha_bd
DB_HOST=localhost
DB_PORT=5432

ALLOWED_HOSTS=["127.0.0.1","localhost"]
```

## 4. Instalar dependências

### 4.1. Ambiente Virtual

Para deixar tudo mais organizado na sua máquina, crie um ambiente virtual próprio para o machine teaching.

Primeiro, instale o `pyenv` seguindo as instruções aqui: https://github.com/pyenv/pyenv#installation

Instale também o plugin `pyenv-virtualenv` seguindo as instruções aqui: https://github.com/pyenv/pyenv-virtualenv#installation

Com o pyenv instalado, baixe uma versão do Python por ele. Por exemplo, vamos baixar o Python 3.10.4:
```
pyenv install 3.10.4
```
Agora, na pasta raiz do repositório, crie um novo ambiente virtual chamado `machine_teaching`, baseado no Python 3.10.4, assim:
```
pyenv virtualenv 3.10.4 machine_teaching
```
Defina esse novo ambiente virtual como o padrão para a pasta do repositório:
```
pyenv local machine_teaching
```

### 4.2. Instalando os pacotes da lista

Basta executar no terminal, na pasta raiz do projeto:

```
pip install -r requirements.txt
```

Se estiver no Mac e o interesse for apenas em extrair dados do BD, no arquivo `requirements.txt` comente a linha:
```
psycopg2
```
Ela deve ficar assim:
```
# psycopg2
```
Fazemos isso para evitar erros de compatibilidade. No pip, quando ocorre um erro de instalação em um pacote, todas as instalações posteriores listadas no `requirements.txt` são comprometidas.

## 5. Carregar os dados do JSON para o BD

### 5.1. Rodando as migrations
Execute, na pasta `machineteaching`:
```
python manage.py migrate 
```

### 5.2. Carregando os dados pré-existentes
Execute, na pasta `machineteaching` (troque `db_2022_05_16.json` pelo nome do JSON que você baixou com os dados do Machine Teaching):
```
python manage.py loaddata db_2022_05_16.json
```

## 6. Colocar o sistema no ar (opcional)

### 6.1. Evitando problemas

No arquivo `machineteaching/machineteaching/settings.py` comente a seguinte linha:
```
CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(",")
```
Ela deve ficar assim:
```
# CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS").split(",")
```

### 6.2. Rodando o servidor

Basta executar, na pasta `machineteaching` do projeto:
```
python manage.py runserver
```

## 7. Explorar o BD pelo DBeaver

Vou ficar devendo uma explicação mais detalhada sobre como acessar o Banco de Dados através do DBeaver, mas se você chegou até aqui não deve ser difícil.

### 7.1. Informações Importantes

* Tabela com os problemas (e função `generate()` dos casos de teste) - `questions_problem`
* Tabela com o "gabarito" de cada problema - `questions_solution`
* Tabela com os casos de teste - `questions_testcase`
* Tabela com as soluções dos usuários - `questions_userlog`

### 7.2. Exemplos de Problemas

* problem_id 820 - Posição da Letra

### 7.3. Recuperando dados de questões pelo id

É possível obter os dados de maneira mais rápida através dos scripts `get_answer.py`, `get_solutions.py` e `get_testcase.py`.

O primeiro passo é passar as configurações do seu banco de dados em cada script (ainda não há um arquivo de configuração).

Depois basta, rodar cada script e conforme solicitado, passar o id da questão desejada.

## 8. Organizar os dados para consumo do Overcode

### 8.0. Clonar o repositório do Overcode Py3

Link do repositório: https://github.com/artsasse/overcode

### 8.1. Gabarito da questão

Crie um arquivo `answer.py` e copie o código "gabarito" da questão para esse arquivo. Ele deve conter apenas o código da função pedida. Exemplo com a função `posLetra`:
```
def posLetra(frase,letra,ocorrencia):
    pos = 0
    contador = 0
    while pos < len(frase):
        if frase[pos] == letra:
            contador = contador + 1
            if contador == ocorrencia:
                return pos
        pos = pos + 1
    return -1
```
Mova esse arquivo para a pasta `ui/data`, dentro da pasta principal do repositório clonado. Se não existir, crie a pasta.

### 8.2. Soluções dos alunos

Faça a mesma coisa do passo anterior com o código de cada aluno para a questão em específico. Cada arquivo deve conter apenas o código da função. Exemplo:
```
def posLetra(frase,letra,numero):
    tamanho=len(frase)
    indice=0
    contagem=0
    while indice<tamanho:
        if frase[indice]==letra:
            contagem+=1
        if contagem==numero:
            return indice
        else:
            return -1
    indice+=1
```

A partir de um JSON exportado com as soluções de todos os alunos para um problema específico, fiz um script para transformar esse JSON em arquivos Python correspondentes a cada solução:
```
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
```
Deixe esses arquivos na pasta `ui/data` também.

### 8.3. Casos de Teste

Colocar um arquivo `testCase.py` na pasta `ui`. Em cada linha do arquivo printar o retorno da função, passando os dados de teste como argumento. Exemplo:
```
print(posLetra('Fui devagar, mas ou o pe ou o espelho traiu-me.', "a", 2))
print(posLetra('Ficou muito tempo com a cara virada para ele.', "e", 3))
print(posLetra('Sao joias viuvas, como eu, Capitu.', "z", 1))
```

## 9. Rodar o Overcode

Executar o script na pasta raiz do Overcode:
```
./run.sh
```
