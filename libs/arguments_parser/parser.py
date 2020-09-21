# -*- coding: utf-8 -*-

import sys
from .base_parser import BaseParser

class Parser(BaseParser):
    '''Classe para parsear opções de linha de comando'''

    
    def __init__(self, argparser, prog_name, base_filename_extractor, file_expander):
        super().__init__(argparser, base_filename_extractor, file_expander)
        self.prog_name = prog_name
        self.parser = self.argparser(prog=self.prog_name, fromfile_prefix_chars='@', 
                                            description='Ajusta arquivos exportados do ' \
                                                         'Tesouro Gerencial a modelos predefinidos e realiza ' \
                                                         'concatenação caso mais de um arquivo seja fornecido. ' \
                                                         'Pode-se passar um arquivo contendo os argumentos: @nome_do_arquivo. ' \
                                                         'Cada linha desse arquivo deve conter apenas um argumento. ' \
                                                         'Os argumentos opcionais devem estar no formato --<nome_arg>=<valor> ' \
                                                         'ou -<abrev_arg>=<valor>, sem espaços.')
        self.parser.add_argument('arquivos', nargs='+', type=str, help='Arquivos. Pelo menos um deve ser ' \
                                                         'informado. pode conter caracteres coringa (*/?) para ' \
                                                         'indicar um conjunto de arquivos.')
        self.parser.add_argument('-m', '--modelo', dest='model', metavar='nome_do_modelo',
                                 type=str, required=True, help='Nome do modelo.')
        self.parser.add_argument('-o', '--destino', dest='output', metavar='arquivo_destino', type=str,
                                 help='Nome do arquivo de saída. Pode conter o caminho completo. Ex: /path/file.csv.')
        self.parser.add_argument('-r', '--remover-duplicatas', dest='remove_duplicates', action='store_true',
                                 default=False, help='Se presente, indica que as duplicatas devem ser removidas.')
        self.parser.add_argument('-d', '--data-unica', dest='date_match', action='store_true', default=False,
                                help='Se presente, indica que as datas de extração dos dados (SIAFI -> TG) ' \
                                'devem ser todas iguais, no caso de múltiplos arquivos.')

    def parse_arguments(self):
        args = self.parser.parse_args()

        files = []
        for file in args.arquivos:
            files += self.file_expander(file)
        
        args.files = list(filter(lambda  x: self.base_filename_extractor(x).replace('.', '') != '' and \
                          self.base_filename_extractor(x) not in ['', self.prog_name] and \
                          not self.base_filename_extractor(x).startswith('~'), files))
        return args