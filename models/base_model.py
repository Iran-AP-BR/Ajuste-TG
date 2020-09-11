# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseModel(ABC):
    '''Classe base para criação de modelos. Qualquer modelo criado deve ser derivado desta classe.
       Todos os métodos abstratos (decorados com @abstractmethod) devem ser sobrescritos.'''

       
    def drop_columns(self, df):
        for col in self.structure:
            col_spec = self.structure.get(col)
            if type(col_spec) == dict and col_spec.get('drop'):
                df = df.drop(col, axis=1)

        return df

    def map_headers(self, df):
        def mapping(col):
            col_spec = self.structure.get(col)            
            name_mapped = col_spec.get('rename') if type(col_spec) == dict else None
            return name_mapped if name_mapped else col
                    
        df.columns = [mapping(col) for col in df.columns]
        return df

    @property
    def dtypes(self):
        types = {}
        for col in self.structure:
            col_spec = self.structure.get(col)
            _type = col_spec.get('type') if type(col_spec) == dict else None
            types[col] = _type if _type else 'str'
            
        return types

    @abstractmethod
    def clean(self, content) -> object:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def header_position(self) -> int:
        pass

    @property
    @abstractmethod
    def offset(self) -> int:
        pass

    @property
    @abstractmethod
    def discard_last_columns(self) -> int:
        pass

    @property
    @abstractmethod
    def fixed_cols(self) -> int:
        pass

    @property
    @abstractmethod
    def functions(self) -> list:
        pass
    
    @property
    @abstractmethod
    def structure(self) -> dict:
        pass
