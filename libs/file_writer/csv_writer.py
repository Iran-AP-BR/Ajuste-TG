# -*- coding: utf-8 -*-

from .base_writer import BaseWriter
import pandas as pd

class CsvWriter(BaseWriter):
    '''Classe especializada em gravar os dados em formato CSV'''

    
    def write(self, data, filename, current_date=None, mode='w', header=True):
        assert mode in ['w', 'a']

        self.errMessage = ''

        try:
            if mode=='w' and current_date:
                current_date_str = current_date.strftime("%d/%m/%Y")
                pd.DataFrame(data={current_date_str: []}).to_csv(filename, mode='w', 
                        compression=self.compression, index=None, encoding=self.encoding,
                        line_terminator=self.line_terminator)

            data.to_csv(filename, mode='a', compression=self.compression, sep=';', quotechar='"', index=None,
                        header=header, encoding=self.encoding, decimal=',', line_terminator=self.line_terminator)
            
        except Exception as e:
            self.errMessage = f'File "{filename}": {e}'
            return False

        return True
    
    def output_filename(self, filename):
        return f'{filename}{self.compression_file_extension}'