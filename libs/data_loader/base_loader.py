# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseLoader(ABC):
    def __init__(self, model, reader):
        self.model = model
        self.reader = reader
        self.errMessage = ''
        self.current_date = None

    @abstractmethod
    def load(self, filename, nrows=None) -> object:
        pass
