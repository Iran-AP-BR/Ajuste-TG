# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseDuplicatesShreder(ABC):
    def __init__(self, encoding='utf-8'):
        self.errMessage = ''
        self.encoding = encoding

    @abstractmethod
    def run(self, original_file=None, final_file=None) -> bool:
        pass

