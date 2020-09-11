# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseParser(ABC):
    def __init__(self, argparser, base_filename_extractor, file_expander):
        self.argparser = argparser
        self.file_expander = file_expander
        self.base_filename_extractor = base_filename_extractor

    @abstractmethod
    def parse_arguments(self) -> object:
        pass
