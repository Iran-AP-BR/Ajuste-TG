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
                'UG Executora.1': {'type': str, 'drop': False, 'rename': 'Nome UG Executora'},
                'UGE - UF': {'type': str, 'drop': False, 'rename': 'UF'},
                'UGE - UF.1': {'type': str, 'drop': False, 'rename': 'Nome UF'},
                'UGE - UG Setorial Auditoria': {'type': str, 'drop': False, 'rename': 'Setorial Auditoria'},
                'UGE - UG Setorial Auditoria.1': {'type': str, 'drop': False, 'rename': 'Nome Setorial Auditoria'},
                'Órgão UGE': {'type': str, 'drop': False, 'rename': 'Órgão'},
                'Órgão UGE.1': {'type': str, 'drop': False, 'rename': 'Nome Órgão'},
                'Nota Empenho CCor': {'type': str, 'drop': False, 'rename': 'Nota Empenho'},
                'NE CCor - Núm. Processo': {'type': str, 'drop': False, 'rename': 'Processo'},
                'NE CCor - Descrição': {'type': str, 'drop': False, 'rename': 'Observação Empenho'},
                'Programa Governo': {'type': str, 'drop': False, 'rename': None},
                'Programa Governo.1': {'type': str, 'drop': False, 'rename': 'Nome Programa Governo'},
                'Ação Governo': {'type': str, 'drop': False, 'rename': None},
                'Ação Governo.1': {'type': str, 'drop': False, 'rename': 'Nome Ação Governo'},
                'PI': {'type': str, 'drop': False, 'rename': 'Plano Interno'},
                'PI.1': {'type': str, 'drop': False, 'rename': 'Nome Plano Interno'},
                'Natureza Despesa Detalhada': {'type': str, 'drop': False, 'rename': 'Natureza Despesa'},
                'Natureza Despesa Detalhada.1': {'type': str, 'drop': False, 'rename': 'Nome Natureza Despesa'},
                'Modalidade Licitação NE CCor': {'type': str, 'drop': False, 'rename': 'Modalidade Licitação'},
                'Modalidade Licitação NE CCor.1': {'type': str, 'drop': False, 'rename': 'Nome Modalidade Licitação'},
                'Inciso NE CCor': {'type': str, 'drop': False, 'rename': 'Inciso'},
                'Favorecido NE CCor': {'type': str, 'drop': False, 'rename': 'Favorecido NE'},
                'Favorecido NE CCor.1': {'type': str, 'drop': False, 'rename': 'Nome Favorecido NE'},
                'Favorecido NE CCor.2': {'type': str, 'drop': False, 'rename': 'Tipo Favorecido NE'},
                'Documento Origem': {'type': str, 'drop': False, 'rename': None},
                'Documento': {'type': str, 'drop': False, 'rename': None},
                'Favorecido Doc.': {'type': str, 'drop': False, 'rename': 'Favorecido Doc'},
                'Favorecido Doc..1': {'type': str, 'drop': False, 'rename': 'Nome Favorecido Doc'},
                'Favorecido Doc..2': {'type': str, 'drop': False, 'rename': 'Tipo Favorecido Doc'},
                'Doc - Observação': {'type': str, 'drop': False, 'rename': None},
                'Dia Lançamento': {'type': str, 'drop': False, 'rename': 'Dia'},
                'Modalidade Aplicação': {'type': str, 'drop': False, 'rename': None},
                'Modalidade Aplicação.1': {'type': str, 'drop': False, 'rename': 'Nome Modalidade Aplicação'},
                'Item Informação': {'type': str, 'drop': True, 'rename': None},
                'DESPESAS LIQUIDADAS (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': 'Despesa Liquidada'},
                'DESPESAS PAGAS (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': 'Despesa Paga'},
                'DESPESAS EMPENHADAS (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': 'Despesa Empenhada'},
                'DESPESAS INSCRITAS EM RPNP (CONTROLE EMPENHO)': {'type': float, 'drop': False, 'rename': 'Despesa Inscrita RPNP'},
                'RESTOS A PAGAR PROCESSADOS INSCRITOS': {'type': float, 'drop': False, 'rename': 'rpp_Inscritos'},
                'RESTOS A PAGAR PROCESSADOS REINSCRITOS': {'type': float, 'drop': False, 'rename': 'rpp_Reinscritos'},
                'RESTOS A PAGAR PROCESSADOS CANCELADOS': {'type': float, 'drop': False, 'rename': 'rpp_Cancelados'},
                'RESTOS A PAGAR PROCESSADOS PAGOS': {'type': float, 'drop': False, 'rename': 'rpp_Pagos'},
                'RESTOS A PAGAR NAO PROCESSADOS INSCRITOS': {'type': float, 'drop': False, 'rename': 'rpnp_Inscritos'},
                'RESTOS A PAGAR NAO PROCESSADOS REINSCRITOS': {'type': float, 'drop': False, 'rename': 'rpnp_Reinscritos'},
                'RESTOS A PAGAR NAO PROCESSADOS CANCELADOS': {'type': float, 'drop': False, 'rename': 'rpnp_Cancelados'},
                'RESTOS A PAGAR NAO PROCESSADOS LIQUIDADOS': {'type': float, 'drop': False, 'rename': 'rpnp_Liquidados'},
                'RESTOS A PAGAR NAO PROCESSADOS PAGOS': {'type': float, 'drop': False, 'rename': 'rpnp_Pagos'},
                'RESTOS A PAGAR NAO PROCESSADOS BLOQUEADOS': {'type': float, 'drop': False, 'rename': 'rpnp_Bloqueados'},
                }
