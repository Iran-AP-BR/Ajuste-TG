# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseWriter(ABC):
    def __init__(self, encoding='utf-8', line_terminator='\n', compression=False):
        self.encoding = encoding
        self.line_terminator = line_terminator
        self.errMessage = ''
        if compression:
            self.compression = 'gzip'
            self.compression_file_extension = '.gz'
        else:
            self.compression = None
            self.compression_file_extension = ''

    @abstractmethod
    def write(self,  data, filename, mode='w', header=True) -> bool:
        pass

    @abstractmethod
    def output_filename(self, filename) -> str:
        pass