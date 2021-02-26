# -*- coding: utf-8 -*-

import pandas as pd
import re

from .base_model import BaseModel


class Model(BaseModel):
    '''Classe utilizada para representar o modelo "execução_despesa" que representa os dados de execução da despesa.'''


    def clean(self, content):
        if type(content) == str:
            content = content.replace(';', ',').strip()
        return content

    @property
    def name(self):
        return 'monitor_gastos'
    
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
        return 35
    
    @property
    def functions(self):
        return []

    @property
    def structure(self):
        return {
                'UG Executora': {'type': str, 'drop': False, 'rename': None},
                'UG Executora.1': {'type': str, 'drop': False, 'rename': 'UG Executora - Desc'},
                'UGE - UF': {'type': str, 'drop': False, 'rename': None},
                'UGE - UF.1': {'type': str, 'drop': False, 'rename': 'UGE - UF - Nome'},
                'UGE - UG Setorial Auditoria': {'type': str, 'drop': False, 'rename': None},
                'UGE - UG Setorial Auditoria.1': {'type': str, 'drop': False, 'rename': 'UGE - UG Setorial Auditoria - Desc'},
                'Órgão UGE': {'type': str, 'drop': False, 'rename': None},
                'Órgão UGE.1': {'type': str, 'drop': False, 'rename': 'Órgão UGE - Desc'},
                'Nota Empenho CCor': {'type': str, 'drop': False, 'rename': None},
                'NE CCor - Núm. Processo': {'type': str, 'drop': False, 'rename': None},
                'NE CCor - Descrição': {'type': str, 'drop': False, 'rename': None},
                'Programa Governo': {'type': str, 'drop': False, 'rename': None},
                'Programa Governo.1': {'type': str, 'drop': False, 'rename': 'Programa Governo - Desc'},
                'Ação Governo': {'type': str, 'drop': False, 'rename': None},
                'Ação Governo.1': {'type': str, 'drop': False, 'rename': 'Ação Governo - Desc'},
                'PI': {'type': str, 'drop': False, 'rename': None},
                'PI.1': {'type': str, 'drop': False, 'rename': 'PI - Desc'},
                'Natureza Despesa Detalhada': {'type': str, 'drop': False, 'rename': None},
                'Natureza Despesa Detalhada.1': {'type': str, 'drop': False, 'rename': 'Natureza Despesa Detalhada - Desc'},
                'Modalidade Licitação NE CCor': {'type': str, 'drop': False, 'rename': None},
                'Modalidade Licitação NE CCor.1': {'type': str, 'drop': False, 'rename': 'Modalidade Licitação NE CCor - Desc'},
                'Inciso NE CCor': {'type': str, 'drop': False, 'rename': None},
                'Favorecido NE CCor': {'type': str, 'drop': False, 'rename': None},
                'Favorecido NE CCor.1': {'type': str, 'drop': False, 'rename': 'Favorecido NE CCor - Desc'},
                'Favorecido NE CCor.2': {'type': str, 'drop': False, 'rename': 'Favorecido NE CCor - Tipo'},
                'Documento Origem': {'type': str, 'drop': False, 'rename': None},
                'Documento': {'type': str, 'drop': False, 'rename': None},
                'Favorecido Doc.': {'type': str, 'drop': False, 'rename': None},
                'Favorecido Doc..1': {'type': str, 'drop': False, 'rename': 'Favorecido Doc. - Desc'},
                'Favorecido Doc..2': {'type': str, 'drop': False, 'rename': 'Favorecido Doc. - Tipo'},
                'Doc - Observação': {'type': str, 'drop': False, 'rename': None},
                'Dia Lançamento': {'type': str, 'drop': False, 'rename': None},
                'Modalidade Aplicação': {'type': str, 'drop': False, 'rename': None},
                'Modalidade Aplicação.1': {'type': str, 'drop': False, 'rename': 'Modalidade Aplicação - Desc'},
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
