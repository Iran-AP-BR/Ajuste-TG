# -*- coding: utf-8 -*-

from .base_reader import BaseReader
'''Classe especializada em abrir arquivos do excel'''


class ExcelReader(BaseReader):
    def read(self, filename, header=None, skiprows=None, dtype=None, nrows=None):
        try:
            self.errMessage = ''
            return self.tool.read_excel(filename, header=header, skiprows=skiprows, dtype=dtype, nrows=nrows)
        
        except Exception as e:
            self.errMessage = f'File "{filename}": {e}'
            return None
        