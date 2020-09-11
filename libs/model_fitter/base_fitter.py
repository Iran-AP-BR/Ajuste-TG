# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod

class BaseFitter(ABC):
    def __init__(self, model, tool):
        self.model = model
        self.tool = tool
        self.errMessage = ''

    @abstractmethod
    def fit(self, data) -> object:
        pass
