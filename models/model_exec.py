# -*- coding: utf-8 -*-

import pandas as pd
import re

from .base_model import BaseModel

def adjustDate(df):
    indexes = df.loc[df['Mês Lançamento'].str.startswith('000/')].index
    df.loc[indexes,'Mês Lançamento'] = 'JAN/' + df['Mês Lançamento'].str[-4:]

    return df


class ModelExec(BaseModel):
    '''Classe utilizada para representar o modelo "execução_despesa" que representa os dados de execução da despesa.'''


    def clean(self, content):
        if type(content) == str and len(re.findall('^\s|\s$|;', content)) > 0:
            content = content.replace(';', ',').strip(' ')
        return content

    @property
    def name(self):
        return 'execução_despesa'
    
    @property
    def header_position(self):
        return 2
    
    @property
    def offset(self):
        return 2
    
    @property
    def discard_last_columns(self):
        return 0

    @property
    def fixed_cols(self):
        return 15
    
    @property
    def functions(self):
        return [adjustDate]

    @property
    def structure(self):
        return {
                'Órgão UGE': {'type': str, 'drop': False, 'rename': None},
                'Órgão UGE.1': {'type': str, 'drop': False, 'rename': 'Órgão UGE - Desc'},
                'UG Executora': {'type': str, 'drop': False, 'rename': None},
                'UG Executora.1': {'type': str, 'drop': False, 'rename': 'UG Executora - Desc'},
                'UGE - UF': {'type': str, 'drop': False, 'rename': None},
                'Programa Governo': {'type': str, 'drop': False, 'rename': None},
                'Programa Governo.1': {'type': str, 'drop': False, 'rename': 'Programa Governo - Desc'},
                'Ação Governo': {'type': str, 'drop': False, 'rename': None},
                'Ação Governo.1': {'type': str, 'drop': False, 'rename': 'Ação Governo - Desc'},
                'Natureza Despesa Detalhada': {'type': str, 'drop': False, 'rename': None},
                'Natureza Despesa Detalhada.1': {'type': str, 'drop': False, 'rename': 'Natureza Despesa Detalhada - Desc'},
                'Modalidade Licitação NE CCor': {'type': str, 'drop': False, 'rename': None},
                'Modalidade Licitação NE CCor.1': {'type': str, 'drop': False, 'rename': 'Modalidade Licitação NE CCor - Desc'},
                'Mês Lançamento': {'type': str, 'drop': False, 'rename': None},
                'Item Informação': {'type': str, 'drop': True, 'rename': None},
                'DESPESAS LIQUIDADAS (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': None},
                'DESPESAS PAGAS (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': None},
                'DESPESAS EMPENHADAS (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': None},
                'DESPESAS INSCRITAS EM RPNP (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR PROCESSADOS INSCRITOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR PROCESSADOS REINSCRITOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR PROCESSADOS CANCELADOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR PROCESSADOS PAGOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR NAO PROCESSADOS INSCRITOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR NAO PROCESSADOS REINSCRITOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR NAO PROCESSADOS CANCELADOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR NAO PROCESSADOS LIQUIDADOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR NAO PROCESSADOS PAGOS': {'type': float, 'drop': False, 'rename': None},
                'RESTOS A PAGAR NAO PROCESSADOS BLOQUEADOS': {'type': float, 'drop': False, 'rename': None},
                }
