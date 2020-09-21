# -*- coding: utf-8 -*-
'''Módulo de definição do classe abstrata BaseModel'''


from abc import ABC, abstractmethod

class BaseModel(ABC):
    '''Classe base para criação de modelos. Qualquer modelo criado deve ser derivado desta classe.
       Todos os métodos ou propriedades abstratos (decorados com @abstractmethod) devem ser sobrescritos.'''

       
    def drop_columns(self, df):
        '''Método responsável pela eliminação de colunas marcadas para serem descartadas, 
        conforme definido na propiedade structure. Via de regra não há necessidade de 
        sobrepor este método.'''

        for col in self.structure:
            col_spec = self.structure.get(col)
            if type(col_spec) == dict and col_spec.get('drop'):
                df = df.drop(col, axis=1)

        return df

    def map_headers(self, df):
        '''método responsável pela renomeação de colunas, conforme definido na propiedade 
        structure. Via de regra não há necessidade de sobrepor este método.'''

        def mapping(col):
            col_spec = self.structure.get(col)            
            name_mapped = col_spec.get('rename') if type(col_spec) == dict else None
            return name_mapped if name_mapped else col
                    
        df.columns = [mapping(col) for col in df.columns]
        return df

    def clean(self, content):
        '''Método para fazer alterações no conteúdo das células, deve ser usada apenas para 
        eliminar ou modificar caracteres ou textos indesejados, ou seja, para fazer a limpeza 
        dos dados, se necessário, caso contrário, não deve ser sobreposto.'''

        return content

    @property
    def dtypes(self):
        '''Propriedade que retornar um dicionário (chave-valor) representativo dos tipos de 
        dados (valor) de cada coluna (chave), conforme definido na propiedade structure. 
        Via de regra não há necessidade de sobrepor esta propriedade.'''

        types = {}
        for col in self.structure:
            col_spec = self.structure.get(col)
            _type = col_spec.get('type') if type(col_spec) == dict else None
            types[col] = _type if _type else 'str'
            
        return types

    @property
    @abstractmethod
    def name(self) -> str:
        '''Propriedade que representa o nome do modelo'''

        pass

    @property
    @abstractmethod
    def header_position(self) -> int:
        '''Número inteiro que indica em que linha estão os cabeçalhos de colunas.'''
    
        pass

    @property
    @abstractmethod
    def offset(self) -> int:
        '''Número inteiro que indica quantas linhas após os cabeçalhos os dados iniciam.'''

        pass

    @property
    @abstractmethod
    def discard_last_columns(self) -> int:
        '''Número inteiro que indica quantos colunas à direita devem ser excluídas.'''

        pass

    @property
    @abstractmethod
    def fixed_cols(self) -> int:
        '''Número inteiro que especifica a quantidade de colunas fixas (à esquerda), ou seja, 
        aquelas que sempre estarão presentes nos arquivos. Pois as colunas de métricas 
        (à direita) podem variar.'''

        pass

    @property
    @abstractmethod
    def functions(self) -> list:
        '''Lista de funções de tratamento de dados a serem executadas durante os ajustes. 
        Por exemplo: mascaramento de CPF, ajuste de formato de data, etc. É opcional, caso 
        não seja necessário, basta retornar uma lista vazia. Essas funcões devem recebe 
        apenas um DataFrame (pandas) como argumento e devem retornar apenas esse DataFrame 
        após o trtamento. Essas funções devem estar definidas fora da classe do modelo.'''

        pass
    
    @property
    @abstractmethod
    def structure(self) -> dict:
        '''Um dicionário (estrutura chave-valor) cujas chaves são os nomes das colunas dos 
        arquivos originais. 
        Colunas sem nome nos arquivos originais devem ser nomeadas na structure com o nome 
        da coluna anterior, acrescida de um ponto e um número sequencial, a partir de 1. Essa 
        contagem reinicia após cada coluna nomeada. Os valores podem ser *None* ou o tipo de dados 
        (str, float, int, etc...), ou ainda um dicionário com as chaves type, drop e rename (todas opcionais). 
        A chave type indica o tipo de dado (o padrão é str), drop indica se a coluna deve ser removida 
        e rename indica um novo nome para a coluna.

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
        
        '''

        pass
