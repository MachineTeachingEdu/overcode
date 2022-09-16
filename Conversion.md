# Convertendo de Python 2 para Python 3

Fiz a conversão utilizando o Python 3.10.4.

## 2to3 - Conversão automática e nativa

Para começar usei o programa 2to3, um conversor de programas em Python 2 para programas em Python 3.

Documentação do 2to3: https://docs.python.org/3/library/2to3.html

Atenção: a biblioteca `lib2to3` na qual esse script é baseado, será removida do Python a partir da versão 3.13.
A sugestão é utilizar as bibliotecas de terceiros `LibCST` ou `parso`.

Esse programa já vem instalado junto com o Python 3. Se, por exemplo, quisermos converter todos os programas de uma pasta e guardar as novas versões em um pasta destino,basta usar o seguinte comando:
```
2to3 --output-dir=pasta_raiz/pasta_destino_python3 -W -n pasta_raiz/pasta_origem_python2 
```
ou
```
python -m lib2to3 --output-dir=pasta_raiz/pasta_destino_python3 -W -n pasta_raiz/pasta_origem_python2 
```
## Corrigindo detalhes

### Imports locais
No arquivo `src/external/pg_logger.py` tive que trocar a linha:
```
import pg_encoder
```
por:
```
from . import pg_encoder
```

Tive que fazer o mesmo no arquivo `src/external/identifier_renamer.py` no import do módulo `ast_extents`.

## Lidando com os imports

No entanto, o 2to3 não consegue resolver problemas de compatibilidade das bibliotecas utilizadas originalmente.

### Métodos descontinuados

#### time.clock()

No arquivo `pipeline_preprocessing.py` tive que trocar o método:
```
time.clock()
```
Por:
```
time.process_time()
```

### Bibliotecas descontinuadas

#### PythonTidy (`PythonTidy.py`) e PyMinifier (`remove_comments.py`)

Tive que trocar essas 2 bibliotecas, usadas pelo Overcode para a limpeza de código, pelas bibliotecas Black e Python Minifier, compatíveis com Python 3.

Essa mudança foi realizada no arquivo `pipeline_default_functions.py`.

### Módulos internos

#### pipeline_old.py
Em `run_pipeline.py` comentei a linha do import do módulo `pipeline_old.py` que não é utilizado no pipeline principal e por isso não foi convertido para Python 3.