# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseWriter(ABC):
    def __init__(self, encoding='utf-8', line_terminator='\n'):
        self.encoding = encoding
        self.line_terminator = line_terminator
        self.errMessage = ''

    @abstractmethod
    def write(self,  data, filename, mode='w', header=True) -> bool:
        pass