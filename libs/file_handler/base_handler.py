# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseHandler(ABC):
    def __init__(self, encoding='utf-8', compressed=False):
        self.compressed = compressed
        self.encoding = encoding

    @abstractmethod
    def open_file(self, filename, mode) -> object:
        pass

    @abstractmethod
    def delete(self, filename):
        pass

    @abstractmethod
    def rename(self, src, dest):
        pass
    
    @abstractmethod
    def mkdir(self, path, file=False):
        pass
