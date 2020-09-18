# ajuste-TG
Script (em python 3.7.5) de ajuste de arquivos exportados do Tesouro Gerencial a modelos predefinidos e realiza concatenação caso mais de um arquivo seja fornecido.

Para adicionar um novo modelo deve-se apenas acrescentar um novo módulo (arquivo .py) dentro de *models*, contendo uma classe chamada **Model**, derivada da classe abstrata **BaseModel**. O nome do arquivo do novo módulo deve ser *model_\<qualquer_coisa\>.py* (e.g.: model_exec.py).


## BaseModel

Os seguintes métodos e propriedade devem ser soprepostos pela nova classe:

* **clean**: método para fazer alterações no conteúdo das células, deve ser usada apenas para eliminar ou modificar caacteres ou textos indesejados.
* **name**: propriedade que representa o nome do modelo.
* **header_position**: número inteiro que indica em que linha estão os cabeçalhos de colunas.
offset: número inteiro que indica quantas linhas após os cabeçalhos os dados iniciam.
* **discard_last_columns**: número inteiro que indica quantos colunas à direita devem ser excluídas.
* **fixed_cols**: número inteiro que especifica a quantidade de colunas fixas (à esquerda), ou seja, aquelas que sempre estarão presentes nos arquivos. Pois as colunas de métricas (à direita) podem variar
* **functions**: lista de funções de tratamento de dados a serem executadas durante os ajustes. Por exemplo: mascaramento de CPF, ajuste de formato de data, etc. É opcional, caso não seja necessário, basta retornar uma lista vazia. Essas funcões devem recebe apenas um DataFrame (pandas) como argumento e devem retornar apenas esse DataFrame após o trtamento. Essas funções devem estar definidas fora da classe do modelo.
* **structure**: um dicionário (estrutura chave-valor) cujas chaves são os nomes das colunas dos arquivos originais.


    > Colunas sem nome nos arquivos originais devem ser nomeadas na *structure* com o nome da coluna anterior, acrescida de um ponto e um número sequencial, a partir de 1. Essa contagem reinicia após cada coluna nomeada. Os valores podem ser *None* ou o tipo de dados (*str*, *float*, *int*, etc...), ou ainda um dicionário com as chaves *type*, *drop* e *rename* (todas opcionais). A chave *type* indica o tipo de dado (o padrão é str), *drop* indica se a coluna deve ser removida e *rename* indica um novo nome para a coluna.
    
    ~~~~
    Exemplo: 

            {
                'Coluna A': {'type': str, 'drop': False, 'rename': None},
                'Coluna A.1': {'type': str, 'rename': 'Valor'},
                'Coluna A.2': {'type': str, 'drop': True},
                'Coluna B': {'drop': False, 'rename': 'Data'},
                'Coluna C': int,
                'Coluna D.1': None,
                'Coluna D.2': {'type': str, 'drop': False},
                }
    ~~~~

## Uso:

* Linha de comando:

    ~~~~
    $ python ajuste_tg.py arquivos [opções]
    ~~~~

* Descrição

    ~~~~
    usage: ajuste_tg [-h] --modelo nome_do_modelo [--destino arquivo_destino]
                    [--remover-duplicatas] [--data-unica]
                    arquivos [arquivos ...]

    positional arguments:
    arquivos              Arquivos. Pelo menos um deve ser informado. pode
                            conter caracteres coringa (*/?) para indicar um
                            conjunto de arquivos.

    optional arguments:
    -h, --help            show this help message and exit
    --modelo nome_do_modelo, -m nome_do_modelo
                            Nome do modelo.
    --destino arquivo_destino, -o arquivo_destino
                            Nome do arquivo de saída. Pode conter o caminho completo.
                            Ex: /path/file.csv.
    --remover-duplicatas, -r
                            Se presente, indica que as duplicatas devem ser removidas.
    --data-unica, -d      Se presente, indica que as datas de extração dos dados
                            (SIAFI -> TG) devem ser todas iguais, no caso de
                            múltiplos arquivos.

    ~~~~

> Em vez de passar os argumentos diretamente, pode-se passá-los por meio de um arquivo: *@nome_do_arquivo*. Cada linha desse arquivo deve conter apenas um argumento. Os argumentos opcionais devem estar no formato --<nome_arg>=<valor_do_argumento> ou -<abrev_arg>=<valor_do_argumento>, não pode haver espaços.

* Exemplo: 

    ~~~~
    $ python ajuste_tg.py @argumentos.txt
    ~~~~

*  *argumentos.txt*

    ~~~~

    dados1/arquivo1.xlsx dados2/*.xlsx
    -m=modelo
    -o=consolidado.csv
    -r
    -d
    ~~~~

## Ambiente Virtual:
É recomendável que se crie um ambiente virtual para executar o projeto. Para fazer isso, deve-se instalar o VirtualEnv, caso ainda não esteja instalado, e criar um ambiente virtual:

* Instalação do VirtualEnv:
    ~~~~
    $ pip install virtualenv
    ~~~~

* Criação do ambiente virtual, sintaxe: virtualenv \<caminho\> (consulte virtualenv -h para mais informações). Exemplo:
    ~~~~
    $ virtualenv venv
    ~~~~

* Acionamento do ambiente virtual:

    ~~~~
    $ venv/scripts/activate
    ~~~~

* Para desativar o ambiente virtual:

    ~~~~
    (venv)$ deactivate
    ~~~~

* Instalação de dependências (após ativar o ambiente virtual):

    ~~~~
    (venv)$ pip install -r requirements.txt
    ~~~~


## Criar executável:
Para criar uma versão executável (.exe) é necessário instalar o *pyinstaller*, preferencialmente dentro do ambiente virtual <span style="font-size: 11px"><sup>Nota</sup></span>.

* Instalação do pyinstaller:
    ~~~~
    (venv)$ pip install pyinstaller
    ~~~~

* Opção 1 -> Criação do executável (.exe) em uma pasta com todos os demais arquivos necessários para a execução:
    ~~~~
    (venv)$ pyinstaller ajuste_tg.py
    ~~~~

* Opção 1 -> Criação do executável em apenas um arquivo .exe:
    ~~~~
    (venv)$ pyinstaller ajuste_tg.py -F
    ~~~~

O resultado estará na pasta *dist*.

>**Nota**: não haverá problema se o *pyinstaller* for instalado fora do ambiente virtual. Porém, a pasta ou o arquivo criados serão desnecessariamente maiores.
