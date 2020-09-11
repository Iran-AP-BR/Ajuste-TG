# -*- coding: utf-8 -*-

from .base_loader import BaseLoader
import re
from datetime import datetime

def get_current_date(indicator):
    indicator = re.findall('(?<=\{).*?\|.*?(?=\})', indicator.strip(), re.U | re.I)[0]
    indicator_list = indicator.split('|')
    str_date = indicator_list[1].strip()
    if not indicator_list or len(indicator_list) != 2:
        raise Exception('Data inválida')
    try:
        current_date = datetime.strptime(str_date, '%d/%m/%Y')
    except:
        raise Exception(f'Data inválida: "{str_date}"')

    return current_date


class Loader(BaseLoader):
    '''Classe para carregar dados de arquivos'''


    def load(self, filename, nrows=None):
        self.errMessage = ''
        self.current_date = ''
        skiprows = [self.model.header_position + r for r in range(1, self.model.offset)]
        fixed_columns_dtypes = None

        try:
            #carrega os dados
            df_data = self.reader.read(filename, header=[0, self.model.header_position], skiprows=skiprows)
            if df_data is None:
                self.errMessage = self.reader.errMessage
                return None

            #obtém a data de extração (SIAFI -> TG)
            self.current_date = get_current_date(df_data.columns[0][0])
            
            #ajusta os cabeçalhos de coluna
            df_data.columns = [col[1] for col in df_data.columns]
            
            #descarta as últimas colunas
            if self.model.discard_last_columns > 0:
                df_data = df_data[df_data.columns[:-self.model.discard_last_columns]]
            
            #atribui tipos de dados às colunas
            model_types = self.model.dtypes
            dtypes = {col: model_types[col] for col in df_data.columns} #Utiliza somente as colunas necessárias
            df_data = df_data.astype(dtypes)

            #verifica a correspondência das colunas fixas
            if list(df_data.columns[:self.model.fixed_cols]) != list(self.model.structure.keys())[:self.model.fixed_cols]:
                self.errMessage = f'Arquivo "{filename}" não corresponde ao modelo (colunas fixas não correspondentes).'
                return None
            
            #verifica a correspondência das colunas variáveis
            variable_cols = list(df_data.columns[self.model.fixed_cols:])
            model_variable_cols = list(self.model.structure.keys())[self.model.fixed_cols:]

            if variable_cols != [] and False in [ h in model_variable_cols for h in variable_cols ]:
                self.errMessage = f'Arquivo "{filename}" não correspoinde ao modelo (colunas variáveis não correspondentes).'
                return None

        except Exception as e:
            self.errMessage = f'Arquivo "{filename}": {e}'
            return None

        return df_data
