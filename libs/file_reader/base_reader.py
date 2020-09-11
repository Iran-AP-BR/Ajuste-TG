# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseReader(ABC):
    def __init__(self, tool):
        self.tool = tool
        self.errMessage = ''

    @abstractmethod
    def read(self, filename, header=None, skiprows=None, dtype=None, nrows=None) -> object:
        pass







