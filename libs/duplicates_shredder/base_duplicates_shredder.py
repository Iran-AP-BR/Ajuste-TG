# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseDuplicatesShredder(ABC):
    def __init__(self, encoding='utf-8', file_handler=None):
        assert file_handler

        self.errMessage = ''
        self.encoding = encoding
        self.file_handler = file_handler

    @abstractmethod
    def run(self, original_file=None, final_file=None) -> bool:
        pass

