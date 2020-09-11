# -*- coding: utf-8 -*-

from .base_writer import BaseWriter

class CsvWriter(BaseWriter):
    '''Classe especializada em gravar os dados em formato CSV'''

    
    def write(self, data, filename, current_date=None, mode='w', header=True):
        assert mode in ['w', 'a']

        self.errMessage = ''

        try:
            if mode=='w' and current_date:
                with open(filename, mode='w', encoding=self.encoding) as fd:
                    fd.write(f'{current_date.strftime("%d/%m/%Y")}\n')

            data.to_csv(filename, mode='a', sep=';', quotechar='"', index=None,
                        header=header, encoding=self.encoding, decimal=',', 
                        line_terminator=self.line_terminator)
            
        except Exception as e:
            self.errMessage = f'File "{filename}": {e}'
            return False

        return True